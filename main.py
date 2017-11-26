import datetime

import fields


class SimpleModel(fields.JsonModel):
    name = fields.String(required=True)
    test_list = fields.List()
    years = fields.Integer()
    salary = fields.Float()
    some_timestamp = fields.Timestamp()
    some_datetime = fields.Datetime()


if __name__ == '__main__':
    simple_model = SimpleModel()
    simple_model.name = "Sławek"
    simple_model.test_list = ["1"]
    simple_model.years = 99
    simple_model.some_timestamp = 15
    simple_model.some_datetime = datetime.datetime.now()
    # simple_model.name = ""

    print(simple_model.years)
