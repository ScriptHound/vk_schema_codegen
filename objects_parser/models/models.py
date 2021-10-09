import abc
from typing import List, Union

from utils.strings_util import resolve_property_name, snake_case_to_camel_case

STANDART_TYPES = ("str", "int", "float")


class ObjectModel(abc.ABC):
    def __init__(self, classname: str, predecessor: str = "BaseModel") -> None:
        self.params: dict = {}
        self.classname: str = classname
        self.predecessor: str = predecessor

    def add_param(self, param_name: str, param_value: str) -> None:
        param_name = resolve_property_name(param_name)
        self.params.update({param_name: param_value})

    def set_super_class(self, predecessor: str):
        self.predecessor = predecessor

    @abc.abstractmethod
    def __str__(self):
        pass


class Annotation(ObjectModel):
    def __init__(
        self,
        classname: str,
        predecessor: str = "BaseModel",
        required: bool = False,
        list_inner_type: Union[str, List[str]] = "default_name",
    ) -> None:
        super().__init__(classname, predecessor=predecessor)
        if isinstance(list_inner_type, list) and len(list_inner_type) == 1:
            list_inner_type = list_inner_type[0]
        self.list_inner_type = list_inner_type
        self.required = required

    @staticmethod
    def type_string_to_default_type(classname: str) -> str:
        classname_copy = classname.replace('"', "").lower()
        if classname_copy == "array":
            return "list"
        elif classname_copy == "boolean":
            return "bool"
        elif classname_copy == "integer":
            return "int"
        elif classname_copy == "number":
            return "float"
        elif classname_copy == "object":
            return "typing.Any"
        elif classname_copy == "string":
            return "str"
        else:
            return classname

    def __unpack_dict_values(self, dictionary: dict):
        return ", ".join(
            self.type_string_to_default_type(v.strip("'")) for v in dictionary.values()
        )

    def __str__(self):
        camel_case_types = snake_case_to_camel_case(self.classname)
        if isinstance(camel_case_types, dict):
            camel_case_types = self.__unpack_dict_values(camel_case_types)
            self.classname = f"typing.Union[{camel_case_types}]".replace(
                "Typing", "typing"
            )
        elif camel_case_types == "Array":
            if isinstance(self.list_inner_type, list):
                self.list_inner_type = [
                    self.type_string_to_default_type(list_inner_type)
                    for list_inner_type in self.list_inner_type
                ]

                self.classname = (
                    "typing.List[typing.Union["
                    + ", ".join(
                        f'"{item}"' if item not in STANDART_TYPES else item
                        for item in self.list_inner_type
                    )
                    + "]]"
                )
            else:
                self.list_inner_type = self.type_string_to_default_type(
                    self.list_inner_type
                )
                self.classname = (
                    "typing.List["
                    + (
                        f'"{self.list_inner_type}"'
                        if self.list_inner_type not in STANDART_TYPES
                        else self.list_inner_type
                    )
                    + "]"
                )
        else:
            self.classname = '"' + camel_case_types + '"'

        self.classname = self.type_string_to_default_type(self.classname)
        if self.required:
            return f": {self.classname}"
        else:
            return f": typing.Optional[{self.classname}]"


class Description(ObjectModel):
    def __str__(self):
        label: str = f'\t"""VK Object {self.classname}'
        if all(desc is None for _, desc in self.params.items()):
            label += '"""\n\n'
            return label

        label += "\n\n"
        for name, description in self.params.items():
            if not description:
                label += f"\t{name} -\n"
            else:
                label += f"\t{name} - {description.strip()}\n"
        label += '\t"""\n\n'
        return label


class ClassForm(ObjectModel):
    def __init__(
        self, classname: str, desc: Description = None, predecessor: str = "BaseModel"
    ) -> None:
        super().__init__(classname, predecessor=predecessor)
        self.description = desc or Description(self.classname)

    def add_description_row(self, name, text):
        self.description.add_param(name, text)

    def add_param(
        self,
        param_name: str,
        param_value: str,
        type: str = None,
        annotation: str = None,
        required=False,
    ) -> None:
        param_name = resolve_property_name(param_name)
        if annotation is not None:
            if type == "array":
                param_name += str(
                    Annotation("array", list_inner_type=annotation, required=required)
                )
            elif not type and isinstance(annotation, list):
                annotations = []
                for item in annotation:
                    if isinstance(item, list):
                        annotations.append(
                            str(
                                Annotation("array", list_inner_type=item, required=True)
                            )[2:]
                        )
                        continue
                    annotations.append(str(Annotation(item, required=True))[2:])
                param_name += str(Annotation(annotations, required=required))
            else:
                param_name += str(Annotation(annotation, required=required))

        self.params.update({param_name: param_value})

    def __str__(self):
        label = f"\n\nclass {self.classname}:\n"
        if self.predecessor is not None:
            label = f"\n\nclass {self.classname}({self.predecessor}):\n"

        label += str(self.description)

        if not self.params:
            label += "\tpass\n"

        for name, value in self.params.items():
            label += f"\t{name} = {value}\n"
        return label
