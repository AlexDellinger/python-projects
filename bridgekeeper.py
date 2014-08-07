def die():
     print ("you are thrown into the gorge of eternal peril")
name = input("what is your name? ")
quest = input("what is your quest? ")

if name== "lancelot":
    color = input ("what is your favorite color? ")
    if color == "blue":
        print("you may pass.")
    else:
        die()
       
elif name == "robin":
    capital = input("what is the capital of assyria")
    if capital == "assur" or capital == "ashur":
        print ("you may pass.")
    else:
        die()
