import random

for i in range(8):
    a = random.randint(0, 100)
    if(a < 60):
        print("You have been deducted after ", i+1, " exams.")
        break
    else:
        print("You pass ", i+1, " exams.")
        if(i == 7):
            print("Congratulations . You get bachelor degree =)")
