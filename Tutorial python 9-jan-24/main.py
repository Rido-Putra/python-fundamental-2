import ast
file_name = " values.txt"

def save_value(input_value, filename):
    with open(filename,"w") as f:
        f.write(input_value)

def load_value(filename):
    with open(filename. "r") as f:
        read = f.read()
    return read

try: 
    value = ast.literal_eval(load_value(file_name))
    print('loaded values:', values) 
except:
    print('creating new file...')
    value = {}

 while True:
    user_input = input ("item / count / print? >>")

    if user_input == "count":
        values["count"] = input('how many >>  ')