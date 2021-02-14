import keyword
import string
import abc
from utils.strings_util import snake_case_to_camel_case


class ObjectModel(abc.ABC):
    def __init__(self, classname: str, predecessor: str = 'BaseModel') -> None:
        self.params: dict = {}
        self.classname: str = classname
        self.predecessor: str = predecessor

    def add_param(self, param_name: str, param_value: str) -> None:
        self.params.update({param_name: param_value})

    def set_super_class(self, predecessor: str):
        self.predecessor = predecessor

    @abc.abstractmethod
    def __str__(self):
        pass


class Annotation(ObjectModel):
    @staticmethod
    def type_string_to_default_type(classname: str) -> str:
        classname = classname.capitalize()
        classname_copy = classname.replace('"', '')
        if classname_copy == 'Integer':
            return 'int'
        elif classname_copy == 'String':
            return 'str'
        elif classname_copy == 'Boolean':
            return 'bool'
        else:
            return classname

    def __unpack_dict_values(self, dictionary):
        types_list = []
        for _, v in dictionary.items():
            v.replace("'", '')
            types_list.append(self.type_string_to_default_type(v))
        return ', '.join(types_list)

    def __str__(self):
        camel_case_types = snake_case_to_camel_case(self.classname)
        if isinstance(camel_case_types, dict):
            camel_case_types = self.__unpack_dict_values(camel_case_types)
            self.classname = f'Union[{camel_case_types}]'
        else:
            self.classname = '"' + camel_case_types + '"'

        self.classname = self.type_string_to_default_type(self.classname)

        label: str = f': Optional[{self.classname}]'
        return label


class Description(ObjectModel):
    def __str__(self):
        label: str = f'\t\"\"\"VK Object {self.classname}\n\n'
        if all(isinstance(desc, type(None)) for _, desc in self.params.items()):
            label += '\t\"\"\"\n'
            return label
        for name, description in self.params.items():
            if description is None:
                description = ""
            label += f'\t{name} - {description}\n'
        label += '\t\"\"\"\n'
        return label


class ClassForm(ObjectModel):
    def __init__(self, classname: str,
                 desc: Description = None,
                 predecessor: str = 'BaseModel'
                 ) -> None:
        super().__init__(classname, predecessor=predecessor)
        self.description = desc if desc else Description(self.classname)

    def add_description_row(self, name, text):
        self.description.add_param(name, text)

    def add_param(self,
                  param_name: str,
                  param_value: str,
                  annotation: str = None
                  ) -> None:
        if annotation is not None:
            param_name += str(Annotation(annotation))

        self.params.update({param_name: param_value})

    def __str__(self):
        label = f'\n\nclass {self.classname}:\n'
        if self.predecessor is not None:
            label = f'\n\nclass {self.classname}({self.predecessor}):\n'    

        label += str(self.description)

        for name, value in self.params.items():
            is_keyword = ''
            if name in keyword.kwlist or name[0] in string.digits:
                is_keyword = '_'
            label += f'\t{is_keyword}{name} = {value}\n'
        return label
