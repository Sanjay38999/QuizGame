name = input("Enter your name: ")
print()
print("Hello", name.upper(), "Welcome to Chemistry QUIZ")
print()

playing = input("Do you wish to continue playing this quiz??: ")
if playing.lower() != "yes":
    quit()

print("Then let's get started :)")
score = 0
print()

i = input("What is the fist element on the periodic table?: ")
if i == "Hydrogen".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Who is the father of Chemistry?: ")
if i == "Antoine Lavoisier" or i == "Lavoisier".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Who is the father of Chemistry in India?: ")
if i == "Chandra Ray".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("What is the name of the element W in chemistry?: ")
if i == "Tungsten".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Which acid is present in lemon?: ")
if i == "Citric acid".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("PVC stands for: ")
if i == "PolyVinyl Chloride".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Which acid is known as the Oil of Vitriol?: ")
if i == "Sulfuric Acid".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Calcium Sulphate is also known as: ")
if i == "Gypsum Salt".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Bleaching action of chlorine is by: ")
if i == "Decomposition".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Which is the heaviest metal?: ")
if i == "Osmium".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Nail polish remover contains: ")
if i == "Acetone".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("What is the charge of a nucleus in an atom?: ")
if i == "Positive".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("What is the charge of an electron in an atom?: ")
if i == "Negative".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("The isotope atoms differ in?: ")
if i == "number of neutrons" or i == "neutrons" or i == "neutron".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Washing soda is: ")
if i == "Sodium Carbonate".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


i = input("Natural rubber is a polymer derived from: ")
if i == "Isoprene".lower():
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()


print("You got", score, "correct answers")
print()

print("Congratulations!!... You have scored " + str((score/16)*100) + "% marks.")




