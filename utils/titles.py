import abc


class AbstractTitle(abc.ABC):
    def __init__(self, **params):
        self.params = params

    @abc.abstractmethod
    def __repr__(self):
        pass


class Imports(AbstractTitle):
    def __repr__(self):
        return (
            "\n".join(
                "from %s import %s" % (k, ", ".join(v)) if v else "import %s" % k
                for k, v in self.params.items()
            )
            + "\n"
        )


class UpdateForwardRefs(AbstractTitle):
    def __repr__(self):
        return (
            "\n\n"
            + (
                "for item in locals().copy().values():"
                "\n\tif inspect.isclass(item) and issubclass(item, BaseModel):"
                "\n\t\titem.update_forward_refs()"
            )
            + "\n"
        )
