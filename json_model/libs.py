import json

from json_model.validators import Validation


class JsonModelBase(type):
    @classmethod
    def __set_fields(cls, namespace):
        namespace['fields'] = []
        for name, attr in namespace.items():
            if hasattr(attr, 'field_type'):
                namespace['fields'].append(name)

        return namespace['fields']

    def __new__(mcs, name, bases, namespace):
        mcs.__set_fields(namespace)
        instance = super().__new__(mcs, name, bases, namespace)
        instance.validation = Validation(namespace['fields'])
        return instance


class JsonModel(metaclass=JsonModelBase):
    def __init__(self, **fields):
        for field, value in fields.items():
            setattr(self, field, value)

    def get_json_fields(self):
        from json_model.fields import ForeignField
        fields = dict()

        for name in self.fields:
            field = getattr(self, name, None)
            if isinstance(field, ForeignField):
                fields[name] = field.value.get_json_fields()
            else:
                fields[name] = field.value

        return fields

    def to_json(self):
        """Returns json object."""
        return json.dumps(self.get_json_fields())


