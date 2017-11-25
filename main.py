import datetime

import fields


class SimpleModel(object):
    name = fields.String(required=True)
    test_list = fields.List()
    years = fields.Integer()
    salary = fields.Float()
    some_timestamp = fields.Timestamp()


if __name__ == '__main__':
    simple_model = SimpleModel()
    simple_model.name = "Sławek"
    simple_model.test_list = ["1"]
    simple_model.some_timestamp = datetime.datetime.now()
    # simple_model.name = ""

    print(simple_model.__dict__)