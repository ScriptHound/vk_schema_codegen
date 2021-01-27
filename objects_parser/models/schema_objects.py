import abc
from .models import ClassForm
from utils.strings_util import get_type_from_reference
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
        for name in prepared_dict[classname]['properties'].keys():
            properties = prepared_dict[classname]['properties']

            if properties[name].get('type', None) == 'array':
                if properties[name]['items'].get('type', None):
                    type_anno = properties[name]['items']['type']
                else:
                    type_anno = properties[name]['items'].get('$ref', None)
                    type_anno = get_type_from_reference(type_anno)
            elif properties[name].get('type', None):
                type_anno = properties[name].get('type', None)
            else:
                type_anno = properties[name].get('$ref', None)
                type_anno = get_type_from_reference(type_anno)

            text = properties[name].get('description', None)
            self.class_form.add_param(name, None, annotation=type_anno)
            self.class_form.add_description_row(name, text)


class SchemaAllOfObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        super_classes_list = []

        for element in prepared_dict[classname]['allOf']:
            properties = element.get('properties', None)
            reference = element.get('$ref', None)

            if properties:
                for name in properties.keys():
                    text = properties[name].get('description', None)
                    self.class_form.add_param(name, None)
                    self.class_form.add_description_row(name, text)
            if reference:
                ref = get_type_from_reference(reference)
                super_classes_list.append(ref)

        self.class_form.set_super_class(",\n\t".join(super_classes_list))


class SchemaEnum(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname, predecessor='enum.Enum')
        for name in prepared_dict[classname]['enum']:
            text = None
            self.class_form.add_param(name.upper(), f'"{name}"')
            self.class_form.add_description_row(name, text)


class SchemaEnumInitialized(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname, predecessor='enum.IntEnum')
        counter = 0
        for i in prepared_dict[classname]['enum']:
            name = prepared_dict[classname]['enumNames'][counter]
            text = None
            self.class_form.add_param(name, i)
            self.class_form.add_description_row(name, text)
            counter += 1


class SchemaUndefined(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)


class SchemaBoolean(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.classname = classname
        self.prepared_dict = prepared_dict

    def __str__(self):
        description = self.prepared_dict[self.classname].get('description', None)
        return f'\n\n{self.classname} = Optional[bool] # {description}\n\n'


def schema_object_fabric_method(classname, prepared_dict):
    json_type = prepared_dict[classname]
    if json_type.get('type', None) == 'object':
        if json_type.get('allOf', None):
            return SchemaAllOfObject(classname, prepared_dict)
        elif json_type.get('properties', None):
            return SchemaObject(classname, prepared_dict)

    elif json_type.get('type', None) == 'string':
        # if enum is numerical
        if type(json_type['enum'][0]) == int:
            return SchemaEnumInitialized(classname, prepared_dict)
        else:
            return SchemaEnum(classname, prepared_dict)

    elif json_type.get('type', None) == 'integer':
        return SchemaEnumInitialized(classname, prepared_dict)

    elif json_type.get('type', None) == 'boolean':
        return SchemaBoolean(classname, prepared_dict)

    elif json_type.get('type', None) is None:
        return SchemaUndefined(classname, prepared_dict)
