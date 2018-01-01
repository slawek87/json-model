import json


class JsonModel(object):
    def get_fields(self):
        from json_model.fields import ForeignField

        fields = dict()

        for name in self.__dir__():
            field = getattr(self, name, None)
            if hasattr(field, 'field_type'):
                if isinstance(field, ForeignField):
                    fields[name] = field.value.get_fields()
                else:
                    fields[name] = field.value

        return fields

    def to_json(self):
        """Returns json object."""
        return json.dumps(self.get_fields())


class Validation(object):
    empty_values = ["", None]

    def __init__(self, field):
        self.field = field
        self.run()

    def run(self):
        validators = [self.validate_empty_values, self.validate_field_type]

        for validator in validators:
            validator()

    def validate_empty_values(self):
        """Checks if value is not None when attribute `required` is True."""
        if self.field.required and self.field.value in self.empty_values:
            error = "Field {field_name} cannot be empty value.".format(field_name=self.field.field_name)
            raise TypeError(error)
        elif not self.field.value:
            return True

    def validate_field_type(self):
        """Checks if given value has correct type."""
        if self.field.value and not isinstance(self.field.value, self.field.field_type):
            error = "Must be a {field_name}".format(field_name=self.field.field_name)
            raise TypeError(error)


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
        self.value = self.unificate_value(value)
        Validation(self)
        instance.__dict__[self.field_name] = self

    def __get__(self, instance, owner):
        Validation(self)
        return self

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

    def unificate_value(self, value):
        """Unificates given value."""
        return value
