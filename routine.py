


print ("Daily Routine check up!")

Wakeup = input("did you wake up at 7:00am? ")
if Wakeup == "yes":
    print ("Good Job!")
else:
    print ("Better luck next time!")

getReady = input("Did you get ready for School?") 
if getReady == "yes":
    print ("Good Job!")
else:
    print("Better luck next time!")

studytime = input("How long did you study for? pls answer in hours!")
if studytime > 2:
    print ("Awesome work! you studied very well today!")
elif studytime < 2:
    print ("You should study more! how will you pass your exams?")
