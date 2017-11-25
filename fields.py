import calendar
import datetime


class Field(object):
    field_type = None
    field_name = None

    empty_values = ["", None]

    def __init__(self, value=None, required=False):
        self.required = required
        self.value = value

    def __get__(self, instance, cls):
        """Returns value if instance was created."""
        if instance:
            return getattr(instance, "value", None)

        return None

    def __set__(self, instance, value):
        """Method sets value if validation is passed."""
        if self.__valid_empty_values__(value):
            return True

        self.__valid_field_type__(value)
        setattr(instance, "value", value)

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
    field_type = "Timestamp"
    field_name = datetime.datetime

    def __set__(self, instance, value):
        """Method sets value if validation is passed."""
        super()
        setattr(instance, "value", calendar.timegm(value.utctimetuple()))


class ForeignField(object):
    pass
