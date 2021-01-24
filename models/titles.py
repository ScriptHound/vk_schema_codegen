import abc


class AbstractTitle(abc.ABC):
    def __init__(self, params={}):
        self.params = params

    @abc.abstractmethod
    def __str__(self):
        pass


class Imports(AbstractTitle):
    def __str__(self):
        import_str = ""
        for k, v in self.params.items():
            if v is None:
                import_str += f'import {str(k)}\n'
            else:
                modules = ', '.join(v)
                import_str += f'from {str(k)} import {str(modules)}\n'
        return import_str


class UpdateForwardRefs(AbstractTitle):
    def __str__(self):
        update_refs_string = "\n"
        for k, _ in self.params.items():
            update_refs_string += f'{k}.update_forward_refs()\n'
        return update_refs_string
