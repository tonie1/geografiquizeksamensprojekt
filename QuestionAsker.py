import random
def askquestions(fname):
    print(fname)

points = 0

questions = ["Switzerland","Germany","Macedonia","Belarus", "United Kingdom","Netherlands","Latvia"]
answers = ["CH","DE","MK","BY","GB","NL","LV"]
wronganswer1 = ["SW","GE","MA","BL","EN","HO","VA"]
wronganswer2 = ["SL","GR","MC","BE","UN","NE","LA"]
wronganswer3 = ["SH","GY","CD","WR","UK","NT","LT"]

randomNumber = random.randint(0,len(questions)-1)

def questionlist():

    print("What two letter abbreviation does  this country have?")
    print(questions[randomNumber])

questionlist()

def questionanswer():

    print("A:" + answers[randomNumber])

questionanswer()

def questionwronganswer1():

    print("B:" + wronganswer1[randomNumber])

questionwronganswer1()

def questionwronganswer2():

    print("C:" + wronganswer2[randomNumber])

questionwronganswer2()

def questionwronganswer3():

    print("D:" + wronganswer3[randomNumber])

questionwronganswer3()

answer = input("Pick an answer: A, B, C or D:")

if answer == "A":
    print("Correct!")
    points += 1

elif answer != "A":
    exit("Wrong answer!")

print('Your score:', points)