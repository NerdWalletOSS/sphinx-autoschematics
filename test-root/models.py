from schematics.types import StringType
from schematics.types.compound import ListType, ModelType
from schematics.models import Model


class SubModel1(Model):
    """This is SubModel1"""
    name = StringType()


class SubModel2(Model):
    """This is SubModel2"""
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

    foo = StringType(required=True, metadata=dict(custom_value=True))

    bar = ListType(StringType)

    sub1 = ModelType(SubModel1)

    sub2 = ListType(ModelType(SubModel2))
