from pydantic import BaseModel, EmailStr, Field
from typing import Optional
#schema
class Student(BaseModel):

    name: str = 'shree' #pass default value
    age: Optional[int] = None #Age can be a number or missing (None), and by default it’s missing
    email: EmailStr  #A special type from Pydantic that validates the string is a proper email format.
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
                  #FIELD:Lets you set extra constraints (like min/max values) and descriptions for a field.

#create a dic
new_student = {'age':'32', 'email':'abc@gmail.com'}
#object
student = Student(**new_student)
#covert obj to dic
student_dict = dict(student)
#from that dic parse and get age to print
print(student_dict['age'])
#This line converts your Pydantic object into a JSON string.
student_json = student.model_dump_json() 
'''
model_dump_json() → Built-in Pydantic method (v2) that serializes the model’s data into JSON format.
Output is a string, not a Python dictionary.
Useful when sending data over APIs or saving into files where JSON is needed.
'''





#for strict validation use :
# roll_number: str = Field(
#         pattern=r'^R\d{3}$',
#         description="Roll number must start with 'R' followed by exactly 3 digits."
#     )


# pattern=... → Uses a regex to strictly control the allowed format.

# ^ → Start of the string.

# R → Must start with the letter R.

# \d{3} → Exactly 3 digits.

# $ → End of the string (nothing extra allowed).

# ✅ Accepts: "R101"
# ❌ Rejects: "101", "R10", "R1001".

# This way, the input must match the exact format, or Pydantic will throw a validation error.