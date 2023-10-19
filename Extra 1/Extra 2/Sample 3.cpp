#include <iostream>

int main()
{
    int x;
    int y;
    int sum;

    std::cout << "Enter the first number: ";
    std::cin >> x;

    std::cout << "Enter the second number: ";
    std::cin >> y;

    if (std::cin.fail()) {
        std::cout << "Invalid input. Please enter numeric values.";
        return 1; // Return an error code
    }

    sum = x + y;

    std::cout << "The sum of the two numbers is: " << sum;

    return 0;
}
