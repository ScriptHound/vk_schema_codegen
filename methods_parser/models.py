from utils.strings_util import (
    camel_case_to_snake_case,
    convert_to_python_type,
    resolve_property_name,
    get_type_from_reference,
)

response_models = {
    "base_bool_response": "base.BoolResponse",
    "base_getUploadServer_response": "base.GetUploadServerResponse",
    "base_ok_response": "base.OkResponse",
}

CLASSMETHOD_PATTERN = (
    "\tasync def {snake_name}(\n"
    "\t\t{args}\n"
    "\t) -> {return_type}Model:\n"
    "\t\t{desc}\n"
    "\t\tparams = self.get_set_params(locals())\n"
    '\t\tresponse = await self.api.request("{name}", params)\n'
    "{model}\n"
    "\t\treturn model(**response).response"
)


class ObjectModel:
    def __init__(self, method_name: str = None, method: dict = None, **params):
        self.method = method
        self.method_name = method_name
        self.params = params


class Description(ObjectModel):
    def __str__(self):
        title = self.method.get("description") or self.method_name + " method"
        descriptions = []
        description = ""
        for param in self.params["sorted_params"]:
            param_description = param.get("description", "").strip()
            descriptions.append(
                f'\t\t:param {param["name"]}:'
                + ((" " + param_description) if param_description else "")
            )

        if descriptions:
            description = "\n" + "\n".join(descriptions) + "\n\t\t"
        return '"""%s%s"""\n' % (title, description)


class Annotation(ObjectModel):
    def __str__(self):
        items = self.params["items"]
        param_type = self.params["type"]
        param_annotate = convert_to_python_type(self.params["annotate"])

        if param_annotate == "list" and items.get("$ref", items.get("type")):
            if items.get("$ref"):
                post_annotate = "str"  # it's enum
            else:
                post_annotate = convert_to_python_type(items["type"])

            param_annotate = "typing.List[%s]" % convert_to_python_type(post_annotate)

        if param_type is False:
            return f"typing.Optional[{param_annotate}] = None"
        return param_annotate


class ConvertToArgs(ObjectModel):
    def __str__(self):
        params = ["self"]
        for param in self.params["sorted_params"]:
            params.append(
                f"{param['name']}: "
                + str(
                    Annotation(
                        annotate=param["type"],
                        type=param.get("required", False),
                        items=param.get("items", {}),
                    )
                )
            )
        params.append("**kwargs")
        formatted = ", ".join(params)

        if len(formatted) >= 80:
            formatted = formatted.replace(", ", ",\n\t\t")

        return formatted


class MethodForm:
    def parse_return_type(m_name, type_response):
        category = m_name.split(".")[0]
        name = get_type_from_reference(type_response.replace(f"{category}_", ""))
        method_name = f"{category}.{name[0].upper() + name[1:]}"
        return_type = type_response.split("/")[-1]
        return response_models.get(return_type, method_name)

    def costruct(**params):
        if params["extended_return_type"]:
            params["model"] = (
                "\t\tmodel = self.get_model(\n"
                '\t\t\t{("extended",): ' + f'{params["extended_return_type"]}' + "},\n"
                f"\t\t\tdefault={params['return_type']},\n"
                "\t\t\tparams=params,\n"
                "\t\t)"
            )
        else:
            params["model"] = f"\t\tmodel = {params['return_type']}"
        return CLASSMETHOD_PATTERN.format(**params)


class ClassForm:
    def __init__(self, classname, predproc="BaseCategory"):
        self.name = classname
        self.predproc = predproc
        self.constructed_methods = []

    def add_method(self, method_name, method):
        sorted_params = sorted(
            method.get("parameters", {}), key=lambda x: not x.get("required", False)
        )
        for item in sorted_params:
            item["name"] = resolve_property_name(item["name"])
        desc = Description(method_name, method, sorted_params=sorted_params)
        args = ConvertToArgs(sorted_params=sorted_params)
        return_type = MethodForm.parse_return_type(
            method_name, method["responses"]["response"]["$ref"]
        )
        extended_type = method["responses"].get("extendedResponse")
        if extended_type:
            extended_type = MethodForm.parse_return_type(
                method_name, extended_type["$ref"]
            )
        self.constructed_methods.append(
            MethodForm.costruct(
                name=method_name,
                snake_name=camel_case_to_snake_case(method_name.split(".")[1]),
                args=args,
                desc=desc,
                return_type=return_type,
                extended_return_type=extended_type,
            )
        )

    def __str__(self):
        return (
            f"\n\nclass {self.name[0].upper() + self.name[1:]}Category({self.predproc}):\n"
            + "\n\n".join(self.constructed_methods)
            + "\n"
        )
