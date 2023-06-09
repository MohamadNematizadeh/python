scores = int(input("enter first score: "))
score_number = 1

while True:
    new_input = input("enter new score: ")
    if new_input != "exit":
        scores = scores + int(new_input)
        score_number = score_number + 1
    else:
        print("is ", str(scores/score_number))
        break