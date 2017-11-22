class Field(object):
    field_type = None

    def __get__(self, instance, owner):
        getattr(instance, self.value)

    def __init__(self):
        self.value = None

    def __set__(self, instance, value):
        if not isinstance(value, self.field_type):
            raise TypeError("Must be a %s" % self.field_type)
        setattr(instance, self.value, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")


class Integer(Field):
    field_type = int


class String(Field):
    field_type = str


class Float(Field):
    field_type = float


class List(Field):
    field_type = list


class TimeStamp(object):
    pass


class ForeignField(object):
    pass
