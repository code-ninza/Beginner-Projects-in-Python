from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import random

imdb_url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating"

#This function will get the movie names from the url  provided.
def movie_list(url):
    movies =[]

    html = urlopen(url)

    soup = BeautifulSoup(html, 'lxml')

    #It will take out all the headings h3 in the website.
    headings = soup.find_all("h3")

    #It will extract the text of those headings and will add them to the list.
    for i in range(50):
        movies.append(headings[i].text)

    #It will remove the unnecessary part of those extracted texts and will store just the movie names in the list.
    for i in range(9):
        movies[i] = movies[i][4:len(movies[i])-8]
    for i in range(9,len(movies)):
        movies[i] = movies[i][5:len(movies[i])-8]

    return random.choice(movies)

#This function will encrytpt the movie  names for the hangman game.
def encryption(word):
    for letter in word:
        if letter in list(string.ascii_letters):
            word = word.replace(letter, "_")
        elif(letter == " "):
            word = word.replace(letter, "/")
        elif (letter.isdigit()):
                word = word.replace(letter, "_")
    return word

#This function is for getting the index of a character if it is in the string.
def getting_indexes(name, list):
    indexe = []
    for i in range(len(list)):
        if(name.lower()==list[i].lower()):
            indexe.append(i)
    return indexe

#This function is the whole setup. It has the algorithm and the necessary to execute the game.
def hangman():
    choices = []
    guesses = 8
    movie_name = movie_list(imdb_url)
    movie_name = movie_name.lower()
    print("The first movie for you to guess is :-")
    temp = encryption(movie_name)
    print(temp)
    print("Your guess is :-")
    flag = True
    while(flag == True):
        if(guesses == 0):
            flag = False
            print("\n\nYou Lost !!! and now you are hanged.")
            print("The movie is "+ movie_name+".")
            break
        elif "_" not in temp:
            flag = False
            print("\n\nWow, Congratulations !!! You won with still "+ str(guesses) +" guesses left.")
            print("The movie is "+movie_name+".")
            break

        user = input()
        user = user.lower()

        if(user not in movie_name):
            if user in choices:
                print("You have already guessed this. Please guess another letter.")
            else:
                guesses -= 1
                print("Ooops!! Wrong guess. You now have "+ str(guesses) +" guess(es) left.")
            print(temp)
        elif user in movie_name:
            indexes = getting_indexes(user, movie_name)
            print("You guessed correct. You still have "+ str(guesses) +" guess(es) left.")
            for i in range(len(indexes)):
                temp = list(temp)
                temp[indexes[i]] = user
                temp = "".join(temp)
            print(temp)

        choices.append(user)

#This function contains the intro and choices for user to play itagain or not. This function runs the game.
def game():
    print("Hello there !! Welcome to Hangman. It's a movie guessing game.\n There are 50 movies to guess. All of them are taken from the first page of 'IMdB top 250 movies based on user rating'.\n Computer will choose a random movie and the game will begin.\n You will have 8 guesses.\nRules :-\n1. You shouldn't guess the same lphabet again(Although game will warn you when you do.)\n2. Wrong guess will decrease you guesses count by 1\n3. Right guess won't make any changes to your guesses count.\n4. You have to type your guess only in lowercase letters.")
    
    print("\n\nThe game starts now ------")
    hangman()
    flag = True
    print("Do you wanna play the game again ?(y/n)")
    while(flag == True):
        user_input = input()
        if(user_input == "y"):
            print("Alright, Here we go.......\n\n")
            hangman()
        else:
            flag = False
            print("You played well !! Bye.")
            break

game()
