import fields


class SimpleModel(object):
    name = fields.String()
    test_list = fields.List()
    years = fields.Integer()
    salary = fields.Float()


if __name__ == '__main__':
    simple_model = SimpleModel()
    simple_model.name = "Sławek"
    simple_model.name = 1

    print(simple_model.name)