my_mood = input("Please write your mood: ")
a_good_mood = "happy"
a_bad_mood = "sad"

if my_mood == a_good_mood: # (if true)
    print("It is great to see you happy")
    print("Only if good mood")

elif my_mood == a_bad_mood:
    print("Only if bad mood")
    print("Hope you feel better")
else:
    print("Only if unknown mood")
    print("Sorry, i don't recognize this mood you're in.")

print("Regardless od the conditional")
print("At the end")


