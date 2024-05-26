import sys

def hello(name, mood):
    print("Hello",name)
    print(f"Your mood is {mood} today!")
    if mood == "Great":
        print("It cant get any better!")
    else:
        print("Do you want me to sing your fav song!")


name = sys.argv[1]
mood = sys.argv[2]
hello(name, mood)
