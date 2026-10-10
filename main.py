def print_args_kwargs(*args, **kwargs):
    print(args)
    for i, value in kwargs.items():
        print(i, value)


print_args_kwargs(1,2,4,6, name='יעל',age=20)


my_dict={"rut":"id=21548751 , age=20","tami":"id=21562652 , age=10","sara":"id=215465224 , age=15"}

def find_student(name,student_dict):
    for key, value in student_dict.items():
        if key == name:
            return value
    return None


print(find_student("tami",my_dict))
print(find_student("sara",my_dict))
print(type(my_dict))


my_dict = {'leah': 'asd',
           'rachel': 12}
print(find_student('leah',my_dict))

