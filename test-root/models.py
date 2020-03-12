from schematics.types import StringType
from schematics.types.compound import ListType
from schematics.models import Model


class ExampleModel(Model):
    """ExampleModel is a model for testing

    Just like in Sphinx .rst files you can use restructured text directives in the
    docstring to provide rich content in the generated docs.

    .. code-block:: yaml

        foo: Foo
        bar:
          - bar1
          - bar2
    """

    foo = StringType(
        required=True,
        metadata=dict(
            custom_value=True
        )
    )

    bar = ListType(StringType)


