from utils.strings_util import camel_case_to_snake_case


dict_choose_models = {
    'base_bool_response': "base.Bool",
    'base_getUploadServer_response': "base.GetUploadServer",
    'base_ok_response': "base.Ok"
}


class Schematik(object):
    def __init__(
        self,
        category_methods: list,
        category_name: str
    ):
        self.methods = category_methods
        self.category_name = category_name

    def return_python_type(self, field):
        if field == 'integer':
            return 'int'
        elif field == 'string':
            return 'str'
        elif field == 'boolean':
            return 'bool'
        elif field == 'array':
            return 'list'
        return field

    def __sort_method_params(self, method_params):
        params = []
        params_ = []
        for param in method_params:
            if param.get("required"):
                params.append(param)
            else:
                params_.append(param)

        return params, params_

    def __parse_params_to_args(self, required, solo):
        params = ['self']
        for param in required:
            params.append(
                f"{param['name']}: {self.return_python_type(param['type'])}")
        for param in solo:
            params.append(
                f"{param['name']}: Optional[{self.return_python_type(param['type'])}] = None")
        params.append("**kwargs")

        formatted = ', '.join(params)
        if len(formatted) >= 80:
            formatted = formatted.replace(', ', ',\n\t\t')
        return formatted

    def __method_documentation_construct(self, method, sorted_params):
        title = method.get(
            "description"
        ) or method['name'] + " method"

        help_params = '\n'.join(
            "\t\t:param %s: %s" % (param['name'], param.get("description", ''))
            for param in sorted_params
        )
        if help_params:
            help_params = '\n' + help_params + '\n\t\t'
        return "\"\"\"%s%s\"\"\"\n" % (title, help_params)

    def __method_case_construct(self, method, method_doc, args):
        method_name = method['name'].split('.')
        returned = dict_choose_models.get(method['responses']['response']['$ref'].split('/')[-1]) or f'{method_name[0]}.{method_name[1][0].upper() + method_name[1][1:]}'
        return f"""
    async def {camel_case_to_snake_case(method['name'].split('.')[1])}(
        {args}
    ) -> {returned}ResponseModel:
        {method_doc}
        params = self.get_set_params(locals())
        response = await self.api.request(\"{method['name']}\", params)
        model = {returned}Response
        return model(**response).response"""

    def method_construct(self, method):
        required, solo = self.__sort_method_params(method.get('parameters', {}))
        all_params = required.copy()
        all_params.extend(solo)

        doc = self.__method_documentation_construct(method, all_params)
        args = self.__parse_params_to_args(required, solo)

        return self.__method_case_construct(method, doc, args)

    @property
    def get(self):
        block_title = "\n\n\nclass %sCategory(BaseCategory):" % self.category_name.capitalize()
        formatted_methods = tuple(
            self.method_construct(method)
            for method in self.methods
        )
        return block_title + '\n'.join(formatted_methods)
