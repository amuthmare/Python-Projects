#known_user = ["Harry","Hermione","Ron","Alice","Chang","Laila","Gini","Sirius"]
#print(len(known_user))

#print("Hi ! I am travis the security bot")
#user = input("What is your name ").strip().capitalize()
#if user in known_user:
#    print("Hello! {}, you are good to go".format(user))

#else:
#    print("Intruder!!!!Ready to tackle!!")


films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }
while True:
    movie_selection = input("Enter you favourite movie? ").strip().title()
    print(movie_selection)
    if movie_selection in films:
        age = int(input("How old are you?").strip())
        if age >= films[movie_selection][0]:
            print("Your movie will be begin soon!!")
        else:
            print("Yor are not old enough for the movie")
    else:
        print("Your movie is not available")
