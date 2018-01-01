import datetime

from json_model.libs import Field, JsonModel


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
