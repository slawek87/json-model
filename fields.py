class Field(object):
    field_type = None
    field_name = None

    empty_values = ["", None]

    def __init__(self, value=None, required=False):
        self.required = required
        self.value = value

    def __get__(self, instance, cls):
        if instance:
            return getattr(instance, "value", None)

        return None

    def __set__(self, instance, value):
        if self.required and value in self.empty_values:
            error = "Field {field_name} cannot be empty value.".format(field_name=self.field_name)
            raise TypeError(error)
        elif not value:
            return None

        if not isinstance(value, self.field_type):
            error = "Must be a {field_name}".format(field_name=self.field_name)
            raise TypeError(error)

        setattr(instance, "value", value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")


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


class TimeStamp(object):
    pass


class ForeignField(object):
    pass
