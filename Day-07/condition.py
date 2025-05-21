import sys

text = sys.argv[1]

if text == "t2.micro":
    print("it will charge 2 dollars per day")
elif text == "t2.medium":
    print("it will charge 4 dollars per day")
elif text == "t2.xlarge":
    print("it will charge 8 dollars per day")

else:
    print("please provide a valied input")