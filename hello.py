import sys

def hello(name, mood):
    print("Hello",name)
    print(f"Your mood is {mood} today!")

name = sys.argv[1]
mood = sys.argv[2]
hello(name, mood)
