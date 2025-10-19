import csv, json
from json import JSONDecodeError

readfile = open('10_01_file.txt', 'r') # r means read
for line in readfile.readlines():
    print(line.strip())

writefile = open('10_01_output.txt', 'w') # w means write
for i in range(10):
    writefile.write(f"line {i}\n")
writefile.close()

appendfile = open('10_01_output.txt', 'a') # a means append
for i in range(10, 20):
    appendfile.write(f"line {i}\n")
appendfile.close()

# with open('10_02_us.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, delimiter='\t')
#     next(reader) # skip csv header
#     for row in reader:
#         print(row)
#
# with open('10_02_us.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter='\t') # prints out csv data as a dictionary
#     next(reader) # skip csv header
#     for row in reader:
#         print(row)

# JSON stuff
jsonString = '''
{
    "name": "John Doe",
    "age": 28,
    "email": "john.doe@example.com",
    "isActive": true,
    "hobbies": ["reading", "cycling", "traveling"],
    "address": {
        "street": "123 Elm St",
        "city": "Somewhere",
        "zip": "12345"
    }
}
'''
try:
    json_dict = json.loads(jsonString)
    print(json_dict)
except JSONDecodeError as e:
    print(f"Error decoding json: {e}")

# Dump JSON
someDictionary = {
    "name": "John Doe",
    "age": 28,
}

json_string_from_dict = json.dumps(someDictionary)
print(json_string_from_dict)
