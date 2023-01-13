import random

score = 0

for i in range(10):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    correct_answer = x * y
    answer = int(input(f"Question {i+1}: {x} x {y} = "))
    if answer == correct_answer:
        print("Right!")
        score += 1
    else:
        print(f"Wrong. The answer is {correct_answer}.")

print(f"You scored {score} out of 10.")
