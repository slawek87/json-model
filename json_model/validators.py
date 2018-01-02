class Validation(object):
    empty_values = ["", None]
    field = None
    fields = None

    def __init__(self, fields):
        self.fields = fields

    def validate(self, field):
        self.field = field

        validators = [self.validate_empty_values, self.validate_field_type]

        for validator in validators:
            validator()

    def validate_empty_values(self):
        """Checks if value is not None when attribute `required` is True."""
        if self.field.required and self.field.value in self.empty_values:
            error = "Field {field_name} cannot be empty value.".format(field_name=self.field.field_name)
            raise TypeError(error)

    def validate_field_type(self):
        """Checks if given value has correct type."""
        if self.field.value and not isinstance(self.field.value, self.field.field_type):
            error = "Given value must be a {field_type} type.".format(field_type=self.field.field_type)
            raise TypeError(error)
