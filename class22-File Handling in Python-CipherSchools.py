'''
File Access Modes
-Read only("r")
-Read and Write("r+")
-Write only("w")
-Write and Read("w+")
-Append only("a")
-Append and write("a+")
'''
file=open("random.txt","w")
file.write("hello, welcome to week 4 of learning sprint")
file.write("\n new line")
file.close()
file=open("random.txt","w")
file.write("shubham khatri")
a=["shubham","vaibhav","karan","harshil","chirag"]
file.writelines(a)
file.close()
file=open("sample.txt","r")
file.read()
print(file.read())
file.close()
# Context Programming
with open("random.txt","r") as file:
    print(file.read())
class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self, *args):
        print("Exitted")
        print(args)
        return True
with A() as x:
    print(x)
    print("inside")
    raise Exception
print("outside")
# JSON files
'''
# html
<html>
<body>
Hello World
</body>
</html>
# Json
{
"html":{
"body":"Hello World"
}
}
'''
a={
    "name":"Shubham",
    "marks":100,
    "languages":[
        "c++",
        "python",
        "go",
        "rust"
    ]
}
import json
s=json.dumps(a)
print(type(s))
print(s)