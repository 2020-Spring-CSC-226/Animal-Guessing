#######################################################################################################################
# Author : Dostonbek Toirov
# Username : toirovd
#
# Project : Animal Guessing Game - tries to find the guessed animal by players by asking the players questions
#           Modified and made more user interactive with using python GUI module - Tkinter
#######################################################################################################################
# Acknowledgements: -
#
#######################################################################################################################

# Imports
from tkinter import *
import json


class AnimalGuess:
    def __init__(self, master, data):
        '''
        Initializing the class attributes and creating some widgets which will be used
        during the whole process of the game. Also, starts the game by calling the method
        intro().
        :param master:
        :param data:
        '''
        self.master = master
        master.title("Animal Guessing Game")        # Sets the title of the window
        self.data = data
        self.text = Label(master)                   # Used to show questions and guess results
        self.play = Button(master)                  # a button to start the game
        self.play_again = Button(master)            # a button to restart the game
        self.intro()                                # a call to intro() method which explains the rules of the game

    def intro(self):
        '''
        Introductory page of the game which explains the rules of the game.
        :return:
        '''
        self.line1 = Label(self.master, text="Animal Guessing Game", font=("Courier", 30), fg='brown', pady=30)
        self.line1.pack()
        self.line2 = Label(self.master, text="Rules are simple: ", font=("Courier", 15), fg='black')
        self.line2.pack()
        self.line3 = Label(self.master, text="You will guess an animal without telling me,", font=("Courier", 12), fg='black', pady=30)
        self.line3.pack()
        self.line4 = Label(self.master, text="And I will try to find it by asking you different questions.", font=("Courier", 12), fg='black')
        self.line4.pack()
        self.line5 = Label(self.master, text="Ready??? Let's begin then!", font=("Courier", 12), fg='black', pady=30)
        self.line5.pack()

        self.play.config(text="Play Now", command=self.start_game, height=2, width=10, bg='green', fg='white', font=20) # Play button
        self.play.pack()

    def start_game(self):
        '''
        Called when the player presses 'Play Now' button. First clears all the widgets on the screen, and
        calls a method to create other necessary widgets.
        :return:
        '''
        self.line1.pack_forget()
        self.line2.pack_forget()
        self.line3.pack_forget()
        self.line4.pack_forget()
        self.line5.pack_forget()
        self.play.pack_forget()
        self.recursive(self.data)       # call to a recursive function
        self.create_widgets()           # call to a create_widgets method

    def recursive(self, data, q="Q"):
        '''
        A method that is called every time player answers a question by saying either 'yes' or 'no'.
        This helps keep going deep down into the data of the dictionary.
        :param data:
        :param q:
        :return:
        '''
        self.text["text"] = data[q]             # text of the text widget is equal to the question
        self.text.config(font=("Courier", 20), height=2, width=200, pady=50)    # designing of the question label
        self.text.pack(side='top')              # showing the text on the screen

    def create_widgets(self):
        '''
        Creates widgets like 'yes', 'no', and 'quit' buttons for a player to interact with the game.
        :return:
        '''
        self.yes = Button(self.master, text="Yes", command=self.yes_clicked, height=3, width=15, bg='green', fg='white', font=20)
        self.yes.pack()
        self.yes.place(x=450, y=180)

        self.no = Button(self.master, text="No", command=self.no_clicked, height=3, width=15, bg='green', fg='white', font=20)
        self.no.pack()
        self.no.place(x=200, y=180)

        self.quit = Button(self.master, text="QUIT", fg="red", command=self.master.quit)
        self.quit.pack(side="bottom")

    def yes_clicked(self, end='no'):
        '''
        Called when the button 'yes' is pressed. Checks if the end of the dictionary is reached; if not, goes even
        deeper into the data of the dictionary and picks up the next question. If the end is reached, then just
        pick up the guess word, and shows it on the screen. Also, asks the player if they want to play again. If they
        do, the game will start from the beginning by calling the main() function.
        :param end:
        :return:
        '''
        answer = "yes"
        if answer in self.data[answer].keys():
            ########### Important Big O Analysis ############
            self.data = self.data[answer]
            self.recursive(self.data)
            #################################################
        else:
            self.text["text"] = "Your guess is " + self.data[answer]["G"]
            self.text.pack()
            self.play_again.config(text="Play Again", command=self.play_again_func, height=2, width=10, bg='green', fg='white',
                             font=20)
            self.play_again.pack()
            self.play_again.place(x=350, y=300)

    def no_clicked(self):
        '''
        Called when the button 'yes' is pressed. Checks if the end of the dictionary is reached; if not, goes even
        deeper into the data of the dictionary and picks up the next question. If the end is reached, then just
        pick up the guess word, and shows it on the screen. Also, asks the player if they want to play again. If they
        do, the game will start from the beginning by calling the main() function.
        :param end:
        :return:
        '''
        answer = "no"
        if answer in self.data[answer].keys():
            ############## Important Big O Analysis #########
            self.data = self.data[answer]
            self.recursive(self.data)
            #################################################
        else:
            self.text["text"] = "Your guess is " + self.data[answer]["G"]
            self.text.pack()
            self.play_again.config(text="Play Again", command=self.play_again_func, height=2, width=10, bg='green', fg='white', font=20)
            self.play_again.pack()
            self.play_again.place(x=350, y=300)

    def play_again_func(self):
        '''
        Called when the user presses 'Play Again' button when the guess word is reached and the game ends. Destroys
        the whole window and restarts from the beginning by calling the main() function.
        :return:
        '''
        self.master.destroy()
        main()


def main():
    '''
    Call to a main function. Used to create the basics of the game, and import needed data and start the game by making
    instances of the game class.
    :return:
    '''

    data = json.load(open('data.json'))  # loads external json file, where all the data is stored

    root = Tk()                          # makes an instance of tkinter module
    root.geometry('800x500+300+50')      # size and opening position of the window
    root.resizable(0,0)                  # ability to resize the game window is set to false, so it will stay static
    game_inst = AnimalGuess(root, data)  # makes an instance of Animal Guess class
    root.mainloop()                      # the ending of the whole process


if __name__ == '__main__':
    main()
