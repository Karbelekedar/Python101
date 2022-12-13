
# open a file in read, write or append mode
# file1 = open("Sample.txt", "a")
# file1.write("Hey this is my first edit ")
#
# file2 = open("Sample.txt", "r")
# print(file2.read())

file1 = open("Sample.txt", "a")

'''
We can go and modify the file when it's in append mode

When you open a file in write mode, it will create a new file if the file is absent
'''

file1.write("Hey it's Kedar's edit")
file1.close()

file = open("Sample.txt","r")
print(file.read())

'''
with open function:
Opens a file within it's local scope and the life-time of that file is the scope of the 'with-open' function


'''
import json


with open("example.json","r") as f:
    data = json.load(f)
    print(data["quiz"]["sport"]["q1"]["question"])


with open("json_dump.json","w") as f:
    d = {
        "configuration": 23,
        "database_port": 3306

    }
    json.dump(d, f)