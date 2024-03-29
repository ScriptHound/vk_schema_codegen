import abc

from utils.strings_util import (
    convert_to_python_type,
    get_annotation_type,
    get_type_from_reference,
)

from .models import Annotation, ClassForm

# fabric method pattern


class AbstractSchemaObject(abc.ABC):
    @abc.abstractmethod
    def __init__(self, classname, prepared_dict):
        pass

    def __str__(self):
        return str(self.class_form)


class SchemaObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        properties = prepared_dict[classname].get("properties")
        required = prepared_dict[classname].get("required", [])
        for name in sorted(properties.keys()):
            type_anno = get_annotation_type(properties[name])

            text = properties[name].get("description")
            self.class_form.add_param(
                name,
                None,
                type=properties[name].get("type"),
                annotation=type_anno,
                required=name in required,
            )
            self.class_form.add_description_row(name, text)


class SchemaAllOfObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        super_classes_list = []

        for element in prepared_dict[classname]["allOf"]:
            properties = element.get("properties")
            required = prepared_dict[classname].get("required", [])
            reference = element.get("$ref")

            if properties:
                for name in sorted(properties.keys()):
                    type_anno = get_annotation_type(properties[name])

                    text = properties[name].get("description")
                    self.class_form.add_param(
                        name,
                        None,
                        type=properties[name].get("type"),
                        annotation=type_anno,
                        required=name in required,
                    )
                    self.class_form.add_description_row(name, text)
            if reference:
                ref = get_type_from_reference(reference)
                super_classes_list.append(ref)
        if super_classes_list:
            formatted = ", ".join(super_classes_list)
            if len(formatted) >= 80:
                formatted = "\n\t" + formatted.replace(", ", ",\n\t") + "\n"
            self.class_form.set_super_class(formatted)


class SchemaOneOfObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        one_of = prepared_dict[classname]["oneOf"]
        references = [element.get("$ref") for element in one_of]
        if all(references):
            self.class_form: ClassForm = ClassForm(classname)
            super_classes_list = []

            for reference in references:
                ref = get_type_from_reference(reference)
                super_classes_list.append(ref)
            if super_classes_list:
                formatted = ", ".join(super_classes_list)
                if len(formatted) >= 80:
                    formatted = "\n\t" + formatted.replace(", ", ",\n\t") + "\n"
                self.class_form.set_super_class(formatted)
        else:
            types = ", ".join(convert_to_python_type(item["type"]) for item in one_of)
            self.class_form = f"\n\n{classname} = typing.Union[{types}]\n"


class SchemaEnum(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(
            classname,
            desc=(
                '\t""" '
                + prepared_dict[classname].get("description", f"{classname} enum")
                + ' """\n\n'
            ),
            predecessor="enum.Enum",
        )
        for name in prepared_dict[classname]["enum"]:
            self.class_form.add_param(name.upper(), f'"{name}"')


class SchemaEnumInitialized(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(
            classname,
            desc=(
                '\t""" '
                + prepared_dict[classname].get("description", f"{classname} enum")
                + ' """\n\n'
            ),
            predecessor="enum.IntEnum",
        )
        for counter, i in enumerate(prepared_dict[classname]["enum"]):
            name = "_".join(
                prepared_dict[classname]["enumNames"][counter].lower().split()
            )
            self.class_form.add_param(name, i)


class SchemaUndefined(AbstractSchemaObject):
    def __init__(self, classname):
        self.class_form: ClassForm = ClassForm(classname)


class SchemaReference(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict, predecessor="BaseModel"):
        if prepared_dict[predecessor].get("type") == "object":
            self.class_form: ClassForm = ClassForm(classname, predecessor=predecessor)
        else:
            self.class_form = f"\n\n{classname} = {predecessor}\n"


class SchemaBoolean(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.classname = classname
        self.prepared_dict = prepared_dict

    def __str__(self):
        description = self.prepared_dict[self.classname].get("description", None)
        return (
            f"\n\n{self.classname} = typing.Optional[bool]"
            + (f"  # {description}" if description else "")
            + "\n"
        )


class SchemaArray(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.classname = classname
        self.prepared_dict = prepared_dict

    def __str__(self):
        description = self.prepared_dict[self.classname].get("description", None)
        items = self.prepared_dict[self.classname].get("items", {})
        annotation = str(
            Annotation(
                "array", list_inner_type=get_annotation_type(items), required=True
            ),
        )[2:]
        return (
            f"\n\n{self.classname} = {annotation}"
            + (f"  # {description}" if description else "")
            + "\n"
        )


def schema_object_fabric_method(classname, prepared_dict):
    json_type = prepared_dict[classname]
    if json_type.get("type") == "object":
        if json_type.get("allOf"):
            return SchemaAllOfObject(classname, prepared_dict)
        elif json_type.get("properties"):
            return SchemaObject(classname, prepared_dict)
        elif json_type.get("oneOf"):
            return SchemaOneOfObject(classname, prepared_dict)

    elif json_type.get("type") == "string":
        # if enum is numerical
        if not json_type.get("enum"):
            return SchemaUndefined(classname)
        elif isinstance(json_type["enum"][0], int):
            return SchemaEnumInitialized(classname, prepared_dict)
        else:
            return SchemaEnum(classname, prepared_dict)

    elif json_type.get("type") == "integer":
        return SchemaEnumInitialized(classname, prepared_dict)

    elif json_type.get("type") == "boolean":
        return SchemaBoolean(classname, prepared_dict)

    elif json_type.get("type") == "array":
        return SchemaArray(classname, prepared_dict)

    elif json_type.get("$ref"):
        predecessor = get_type_from_reference(json_type["$ref"])
        return SchemaReference(classname, prepared_dict, predecessor)

    elif json_type.get("type") is None:
        return SchemaUndefined(classname)
