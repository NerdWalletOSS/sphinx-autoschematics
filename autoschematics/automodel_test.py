from schematics.types import StringType
from schematics.types.compound import ListType
from schematics.models import Model

from autoschematics.automodel import as_annotation, full_model_class_name, humanize


def test_humanize():
    assert humanize("employee_salary") == "Employee salary"


def test_full_model_class_name():
    class MyModel(Model):
        pass

    assert full_model_class_name(MyModel) == "autoschematics.automodel_test.MyModel"


def test_as_annotation():
    assert as_annotation(StringType()) == "StringType()"
    assert as_annotation(ListType(StringType)) == "ListType(StringType())"
