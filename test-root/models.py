from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ListType, ModelType


class SubModel1(Model):
    """This is SubModel1's docstring"""

    name = StringType()


class SubModel2(Model):
    """This is SubModel2's docstring"""

    name = StringType()


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
            custom_value=True, another_value=dict(one="1", two="2", apple="3")
        ),
        choices=("fizz", "buzz"),
    )

    #: This is bar's docstring
    bar = ListType(StringType)

    sub1 = ModelType(SubModel1, metadata=dict(description="This is sub1's docstring"))

    sub1a = ModelType(SubModel1)

    sub2 = ListType(ModelType(SubModel2))

    sub2_with_default = ListType(
        ModelType(SubModel2), default=[SubModel2({"name": "default_name"})]
    )

    #: Secret will not be documented
    secret = StringType(metadata=dict(document=False))
