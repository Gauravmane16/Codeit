# Old-style Python code
import random

def GuessTheNumber():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)#include <iostream.h>

int main()
{
    int x;
    int y;
    int sum;
    
    cout << "Enter the first number: ";
    cin >> x;
    
    cout << "Enter the second number: ";
    cin >> y;
    
    sum = x + y;
    
    cout << "The sum of the two numbers is: " << sum;
    
    return 0;
}

    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

if __name__ == "__main__":
    GuessTheNumber()
