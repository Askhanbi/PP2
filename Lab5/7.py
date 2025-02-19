import re 

def to_snake(s):
    return re.sub(r"(?<!^)([A-Z])", r"_\1", s).lower()

string = input()

print(to_snake(string))
# HelloWorld <---  Hello_World

