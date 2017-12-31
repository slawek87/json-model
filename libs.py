import json


def JsonHandler(field):
    if hasattr(field, '__dict__'):
        return field.__dict__
    else:
        raise TypeError


class JsonModel(object):
    def to_json(self):
        """Returns json object."""
        return json.dumps(self.__dict__, default=JsonHandler)


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
        instance.__dict__[self.__name] = self.unificate_value(value)

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

    def unificate_value(self, value):
        """Unificates given value."""
        return value
