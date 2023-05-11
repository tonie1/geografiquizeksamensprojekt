def askquestions(fname):
    print(fname)

askquestions("a: ch")
askquestions("b: dk")
askquestions("c: ca")
askquestions("d: pl")

##answers

questionone = input("What country code does Switzerland use?")

if questionone == "a":
    print("Correct!")

elif questionone == "b":
    exit("Wrong answer!")

elif questionone == "c":
    exit("Wrong answer!")

elif questionone == "d":
    exit("Wrong answer!")