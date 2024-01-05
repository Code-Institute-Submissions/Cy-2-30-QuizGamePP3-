from colorama import Fore
import classes
import time 


def gameIntro():
    """
    Welcome message
    """
    print(Fore.RED + "Welcome to... ")
    print(Fore.GREEN + "Who is in the Festive Spirit?" + Fore.RED + " quiz game!")
    print(Fore.CYAN +"******************************\n")
    time.sleep(5)

gameIntro()


def gameRules():
    """
    Game instructions and rules
    """
    print(Fore.RED +"Game Rules!")
    print(Fore.CYAN +"******************************" + Fore.GREEN )
    print("\nThere are 20 questions in total to complete the game.")
    print("\nThere are 3 guesses allocated, to complete all questions.")
    print("\nIf all guesses are finished, ")
    print("\nafter each wrong answer the game will pass to the next question.")  
    print("\nThere is a timer when completing the questions.")
    print("\nThe score percentage would be given at the end with ratings compared")
    print("\nto other players.")  
    print(Fore.CYAN +"******************************\n")
    time.sleep(3)
    print(Fore.MAGENTA + "Extra Notes!")
    print(Fore.CYAN +"******************************" + Fore.MAGENTA)
    print("\nThere are random facts about the game, ")
    print("\nWhich some of them give hints to some questions in the game.")
    print("\nKeep your eyes open for those hints!") 
    print(Fore.CYAN +"******************************\n")
    time.sleep(5)
    
gameRules()


def checkAlpha():
    """
    Checks for alphabets in the name
    """

checkAlpha()


def checkNum():
    """
    Checks for numbers in the name
    """

checkNum()


def checkCharc():
    """
    Checks for number of charectors in the name
    """

checkCharc()


def questions():
    """
    It pulls questions and displays in
    """

question()


def guess():
    """
    Checks number of guesses
    """

guess()


def addStats():
    """
    Add score to the google sheets
    """

addstats()


def pullStats():
    """
    Pulls stats from google sheets 
    """

pullStats()