import random

answers = ['yes', 'no', 'ask later', 'maybe', 'do not count on it',] 

print("Welcome to the mystical magic eight ball.")


while True:
    print("ask a question")
    question = input('>')
    if 'die' in question:
        print ('your a B****!')
    answer = random.choice(answers)
    print(answer)
