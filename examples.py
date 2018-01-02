import datetime
import time

from json_model import fields
from json_model import libs


class Scholarship(libs.JsonModel):
    amount = fields.Float(required=True)
    currency = fields.String(default='USD')
    months = fields.List(required=True)


class Student(libs.JsonModel):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    age = fields.Integer()
    day_of_birth = fields.Datetime()
    scholarship = fields.ForeignField()

    created_at = fields.Timestamp()


if __name__ == '__main__':
    scholarship = Scholarship()
    scholarship.amount = 500.00
    scholarship.months = [1, 2, 3, 4, 5, 8, 9, 10]

    student = Student()
    student.name = "Andrew"
    student.surname = "Gardner"
    student.age = 26
    student.day_of_birth = datetime.datetime.strptime('Jun 1 1999  1:33PM', '%b %d %Y %I:%M%p')

    student.scholarship = scholarship

    student.created_at = int(time.time())

    print(student.to_json())
