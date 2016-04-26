setup = "dr"
punchline = "you just said it!"

print("Computer: Knock, knock...")

while True:
    response = input("You: ")
    if response == "Who's there?":
        break;
    print("Computer: Huh? Do you even know how these jokes work?")
    
print("Computer:", setup)

while True:
    response = input("You: ")
    if response == setup+" who?":
        break;
    print("Computer: You really don't get these jokes, do you?")

print("Computer:", punchline)
