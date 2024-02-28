import random
def bool2string(value):
    return "This was your boolean value :" + str(value) 

boolean_value = random.choice([True, False])
string_value = bool2string(boolean_value)
print(string_value)