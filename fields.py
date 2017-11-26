import datetime


class JsonModel(object):
    pass


class Field(object):
    field_type = None
    field_name = None

    empty_values = ["", None]

    def __init__(self, default=None, required=False):
        self.required = required
        self.value = default

    def __set_name__(self, owner, name):
        self.__name = name

    def __set__(self, instance, value):
        """Method sets value if validation is passed."""
        if self.__valid_empty_values__(value):
            return True

        self.__valid_field_type__(value)
        instance.__dict__[self.__name] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

    def __valid_empty_values__(self, value=None):
        """Checks if value is not None when attribute `required` is True."""
        if self.required and value in self.empty_values:
            error = "Field {field_name} cannot be empty value.".format(field_name=self.field_name)
            raise TypeError(error)
        elif not value:
            return True

    def __valid_field_type__(self, value):
        """Checks if given value has correct type."""
        if not isinstance(value, self.field_type):
            error = "Must be a {field_name}".format(field_name=self.field_name)
            raise TypeError(error)


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


class ForeignField(Field):
    field_name = "Datetime"

    def __init__(self, foreign_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_type = foreign_model
