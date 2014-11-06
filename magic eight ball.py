import random

answers = ['yes', 'no', 'ask later', 'maybe','welcome to the dark side', 'do not count on it','the cow says moo','shut up','i am a phyco killer who will show up at yo house in a turd suit'] 

print("Welcome to the mystical magic eight ball.")


while True:
    print("ask a question")
    question = input('>')
    if 'die' in question:
        print ('your a B****!')
    answer = random.choice(answers)
    print(answer)
    if 'awesome' in question:
        print ('you suck!!!!!')
