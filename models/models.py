import keyword
import string
import abc


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
