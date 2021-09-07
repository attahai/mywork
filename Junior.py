"""This simulates an interaction between a Grown-up
and an 8 year old who keeps on asking questions"""


ask_junior = " "
while ask_junior != "Stop it!":
    ask_junior = input("Grown-up: ") #start a simple conversation
    if ask_junior == "Stop it!":
        response = "Junior: Ok Boss"
        print(response)
        break
    else:
        print("Junior:\t Why?")  