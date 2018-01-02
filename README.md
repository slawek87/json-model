# Json-Model

Json-Model is simple library to create Json Models from Python Objects. Library supports field validation by Python Types and required fields.

# Usage

Usage is really simple. Json-Model on this moment supports 7 basics fields:
    - `Integer`
    - `String`
    - `Float`
    - `List`
    - `Timestamp`
    - `Datetime`
    - `ForeignField`

Each field has attribute:
    - `required` - Boolean attribute in default is set to `False`.
    - `default` - set default value when field is empty.

To start work with JsonModel, create Json-Model class with all fields what you need in Json object.

```python
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
```
