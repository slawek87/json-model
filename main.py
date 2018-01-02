import datetime

from json_model import fields
from json_model import libs


class SimpleModel2(libs.JsonModel):
    name = fields.String(required=True)
    test_list = fields.List()


class SimpleModel(libs.JsonModel):
    name = fields.String(required=True)
    test_list = fields.List()
    years = fields.Integer()
    salary = fields.Float()
    some_timestamp = fields.Timestamp()
    some_datetime = fields.Datetime()

    # foreign = fields.ForeignField(SimpleModel2)


if __name__ == '__main__':
    simple_model2 = SimpleModel2()
    simple_model2.name = "Slawek 1"

    simple_model = SimpleModel()
    simple_model.name = "Slawek"
    simple_model.test_list = ["1"]
    simple_model.years = 99
    simple_model.some_timestamp = 15
    simple_model.some_datetime = datetime.datetime.now()

    # simple_model.name = ""

    # print(simple_model.foreign.name)
    # print(simple_model.years.value)
    print(simple_model.to_json())
    # print(simple_model)

    # simple_model = SimpleModel(**{'name': 'slawek', 'elo': 2})
    # print(simple_model.to_json())
    #
    # print(simple_model.name)
