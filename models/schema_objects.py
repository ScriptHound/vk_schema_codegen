import abc
from .models import ClassForm


class AbstractSchemaObject(abc.ABC):
    @abc.abstractmethod
    def __init__(self, classname, prepared_dict):
        pass


class SchemaObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        for name in prepared_dict[classname]['properties'].keys():
            text = prepared_dict[classname]['properties'][name].get('description', 'No description')
            self.class_form.add_param(name, None)
            self.class_form.add_description_row(name, text)

    def __str__(self):
        return str(self.class_form)


class SchemaAllOfObject(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        for element in prepared_dict[classname]['allOf']:
            properties = element.get('properties', None)
            if properties:
                for name in properties.keys():
                    text = properties[name].get('description', 'No description')
                    self.class_form.add_param(name, str(iter))
                    self.class_form.add_description_row(name, text)

    def __str__(self):
        return str(self.class_form)


class SchemaEnum(AbstractSchemaObject):
    def __init__(self, classname, prepared_dict):
        self.class_form: ClassForm = ClassForm(classname)
        counter = 0
        for name in prepared_dict[classname]['enum']:
            text = None
            self.class_form.add_param(name, str(counter))
            self.class_form.add_description_row(name, text)
            counter += 1

    def __str__(self):
        return str(self.class_form)
