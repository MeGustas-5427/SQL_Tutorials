import typing
from enum import Enum, EnumMeta


class ChoiceEnumMeta(EnumMeta):
    def __getattribute__(cls, name: str) -> typing.Any:
        attr = super().__getattribute__(name)
        if isinstance(attr, Enum):
            return attr.value
        return attr

    def __iter__(cls):
        if hasattr(cls, "__admin__"):
            admin = cls.__admin__()
            return (
                (tag.value, admin.get(tag.name, tag.name)) for tag in super().__iter__()
            )
        return ((tag.value, tag.name) for tag in super().__iter__())

    def iter(cls):
        return ((tag.value, tag.name) for tag in super().__iter__())


class ChoiceEnum(Enum, metaclass=ChoiceEnumMeta):
    """
    Enum for Django ChoiceField use.

    Usage::
        ```
        class MyModel(models.Model):
            class Languages(ChoiceEnum):
                Chinese = "ch"
                English = "en"
                French = "fr"

            language = models.CharField(max_length=20, choices=Languages)
        ```

        It is equivalent to the definition below

        ```
        class MyModel(models.Model):
            Languages = (
                ("ch", "Chinese")
                ("en", "English")
                ("fr", "French")
            )

            language = models.CharField(max_length=20, choices=Languages)
        ```
    """


if __name__ == "__main__":

    class Languages(ChoiceEnum):
        Chinese = "ch"
        English = "en"
        French = "fr"

    for language in Languages:
        print(language)

    print(Languages.Chinese, type(Languages.Chinese))
