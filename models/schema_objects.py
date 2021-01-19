import abc
from .models import ClassForm


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
            text = prepared_dict[classname]['properties'][name].get('description', None)
            self.class_form.add_param(name, None)
            self.class_form.add_description_row(name, text)


class SchemaAllOfObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        for element in prepared_dict[classname]['allOf']:
            properties = element.get('properties', None)
            if properties:
                for name in properties.keys():
                    text = properties[name].get('description', None)
                    self.class_form.add_param(name, str(iter))
                    self.class_form.add_description_row(name, text)


class SchemaEnum(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        counter = 0
        for name in prepared_dict[classname]['enum']:
            text = None
            self.class_form.add_param(name, str(counter))
            self.class_form.add_description_row(name, text)
            counter += 1


class SchemaEnumInitialized(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        counter = 0
        for i in prepared_dict[classname]['enum']:
            # minus one because numerical enum starts from 1
            name = prepared_dict[classname]['enumNames'][counter]
            text = None
            self.class_form.add_param(name, i)
            self.class_form.add_description_row(name, text)
            counter += 1


class SchemaUndefined(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)


def schema_object_fabric_method(classname, prepared_dict):
    if prepared_dict[classname].get('type', None) == 'object':
        if prepared_dict[classname].get('allOf', None):
            return SchemaAllOfObject(classname, prepared_dict)
        elif prepared_dict[classname].get('properties', None):
            return SchemaObject(classname, prepared_dict)

    elif prepared_dict[classname].get('type', None) == 'string':
        # if enum is numerical
        if type(prepared_dict[classname]['enum'][0]) == int:
            return SchemaEnumInitialized(classname, prepared_dict)
        else:
            return SchemaEnum(classname, prepared_dict)

    elif prepared_dict[classname].get('type', None) == 'integer':
        return SchemaEnumInitialized(classname, prepared_dict)

    elif prepared_dict[classname].get('type', None) is None:
        return SchemaUndefined(classname, prepared_dict)
