import random

class NumberGuesser():
    def __init__(self, name):
        self.name = name
        self.min = 1
        self.max = 100
        self.number_of_guesses = 1
        self.hint_count = 0
        self.total_hints = 3
        self.hints_recieved = []
        self.your_hints = []
    
    def welcome_menu(self):
        try:
            print("")
            print("Choose an option: ")
            print("1. Start game")
            print("2. Change the range of numbers the guessing game")
            print("3. How to play?")
            print("4. Quit")
            choice = int(input(""))
            if choice == 1:
                number = random.randint(self.min, self.max)
                print(self.name, "I am thinking of a number between ", self.min, " and ", self.max)
                self.start_game(number)
            elif choice == 2:
                self.change_min_max()
            elif choice == 3:
                self.help()
            elif choice == 4:
                self.quit()
            else:
                print("Please enter a choice between 1 and 4")
                self.welcome_menu()
        except ValueError:
            print("Plese enter a valid choice")
            self.welcome_menu()

    
    def start_game(self, number):
        print()
        valid_guess = False
        while valid_guess == False:
            try:
                guess = int(input("Please enter your guess: "))
                valid_guess = True
            except ValueError:
                print("Please enter a valid integer")
                valid_guess = False
            # self.start_game(number)

        while guess != number:
            if guess < number:
                print("Your guess is lesser than the number")
                self.number_of_guesses += 1
                self.wrong_guess(number)
            if guess > number:
                print("Your guess is higher than the number")
                self.number_of_guesses += 1
                self.wrong_guess(number)
            else:
                print("Corresct gueess ", self.name, "The number was ", number)
                print("You guessed in ", self.number_of_guesses, " tries")
                self.quit()

    def change_min_max(self):
        try:
            new_min = int(input("Please enter the new min: "))
            new_max = int(input("Please enter the new max: "))
            if new_min == new_max:
                print("min and max can not be equal, please try again: ")
                print("")
                self.change_min_max()
            if new_min > new_max:
                print("min can not be greater than max, please try again")
                print("")
                self.change_min_max()
            self.min = new_min
            self.max = new_max
            self.welcome_menu()
            
        except ValueError:
            print("Plese enter a valid integer")
            self.change_min_max()
    
    def help(self):
        print("")
        self.welcome_menu()
    
    def wrong_guess(self, number):
        try:
            print()
            print("1. Take another guess")
            print("2. Hint: You have", self.total_hints - self.hint_count, "remaining")
            print("3. End Game")
            choice = int(input(""))
            if choice == 1:
                # return
                self.start_game(number)
            elif choice == 2:
                if self.total_hints - self.hint_count > 0:
                    self.hint_count += 1
                    print("Hint number ", self.hint_count, ":")
                    self.hint(number)
                    remaining_hint = self.total_hints - self.hint_count
                    print("You have ", remaining_hint, " hints remaining")
                    # self.start_game(number)
                    # return
                else:
                    print("You have exhausted all your hints")
                    print("Your hints were:")
                    for hint in self.your_hints:
                        print(hint)
                    # return
                    # self.start_game(number)
            elif choice == 3:
                print("The number is ", number)
                print("Thanks for playing")
                self.quit()
            else:
                print("please enter a valid choice")
                self.wrong_guess(number)
        except ValueError:
            print("Please enter a valid choice")
            self.wrong_guess(number)


    def hint(self, number):
        hint_number = random.randint(1, self.total_hints)
        if hint_number not in self.hints_recieved:
            self.hints_recieved.append(hint_number)
            if hint_number == 1:
                    self.odd_even(number)
            if hint_number == 2:
                    self.between(number)
            if hint_number == 3:
                    self.prime_multiple(number)
            # self.start_game(number)
        else:
            self.hint(number)
   
    def odd_even(self, number):
        if number%2 == 0:
            hint = ("It is an even number")
        else:
            hint = ("It is an odd number")
        self.your_hints.append(hint)
        print(hint)
    
    def between(self, number):
        range_min = number - random.randint(7,15)
        range_max = number + random.randint(7,15)
        hint = "The number is between " + str(range_min) + " and "+ str(range_max)
        self.your_hints.append(hint)
        print(hint)
    
    def prime_multiple(self, number):
        flag = False
        if number <= 1:
            print("The number is 1 or les than 1")
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    flag = True
                    break
        if flag:
            hint = "The number is not a prime number"
        else:
            hint = "The number is a prime number"
            self.your_hints.append(hint)
            print(hint)
    
    def quit(self):
        print("See you later,", self.name)

if __name__ == '__main__':
    print("Welcome to the number guesser game!")
    name = input("Please enter your name: ")
    game = NumberGuesser(name)
    game.welcome_menu()
