print("Math Facts Game")
print()
multiples = int(input("Name your multiples: "))
print()
counter = 0
for i in range(1, 11):
    correct_answer = i * multiples
    print(i, "x", multiples)
    answer = int(input("> "))
    if answer == correct_answer:
        print("You got it right!")
        counter += 1
    else:
        print("That's not correct. It should have been", correct_answer)
    print()
if counter == 10:
    print("Wow! A perfect score! 🥳")
elif counter == 0:
    print("You got none right. 😭")
elif counter >= 5:
    print("You got", counter, "out of 10 correct.")
else:
    print("You can do better. You got", counter, "out of 10 correct.")
  
