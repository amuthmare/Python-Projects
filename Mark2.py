#while True:
#    question = input("why is the sky blue???? ").strip()
#    if "Just because" in question:
#        print(question)
#    else:
#        print("You think I am a fool")

#vowels = 0
#consonants = 0
#blankSpace = 0
#statement = input("Enter some words to check vowels and consonants? ").strip().lower()
#for letter in statement:
#    if letter in "aeiou":
#        vowels = vowels + 1
#        print(letter)
#    elif letter in " ":
#        blankSpace = blankSpace + 1
#    else:
#        consonants = consonants + 1
        #print(letter)
#print("There are {} vowels in the statement".format(vowels))
#print("There are {} consonants in the statement".format(consonants))
#print("There are {} blank spaces in the statement".format(blankSpace))


students = {"male":["Aditya","Sanjyot","Atharva","Onkar","Keshav","Tom","Leo","Lucifer"],
            "female":["Ankita","Vrushali","Lolita","Priya","Sheena"]}
for key in students.keys():
    for name in students[key]:
        if "A" in name:
            print(name)
