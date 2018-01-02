import datetime

from json_model.libs import JsonModel
from json_model.validators import Validation


class Field(object):
    field_type = None
    field_name = None

    def __init__(self, default=None, required=False):
        self.required = required
        self.value = default

    def __set_name__(self, owner, name):
        self.field_name = name

    def __set__(self, instance, value):
        """Method sets value if validation is passed."""
        setattr(self, 'value', value)
        instance.validation.validate(self)
        setattr(self, 'value', self.unificate_value(value))
        instance.__dict__[self.field_name] = self

    def __get__(self, instance, owner):
        Validation(self)
        return self

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

    def unificate_value(self, value):
        """Unificates given value."""
        return value


class Integer(Field):
    field_type = int
    type_name = "Integer"


class String(Field):
    field_type = str
    field_name = "String"


class Float(Field):
    field_type = float
    field_name = "Float"


class List(Field):
    field_type = list
    field_name = "List"


class Timestamp(Field):
    field_type = int
    field_name = "Timestamp"


class Datetime(Field):
    field_type = datetime.datetime
    field_name = "Datetime"

    def __init__(self, datetime_format="%Y-%m-%d %H:%M:%S", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datetime_format = datetime_format

    def unificate_value(self, value):
        return value.strftime(self.datetime_format)


class ForeignField(Field):
    field_name = "ForeignField"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_type = JsonModel
