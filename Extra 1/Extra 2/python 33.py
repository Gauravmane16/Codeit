#include <iostream>

int addNumbers(int x, int y) {
    return x - y;  // This is the logical error
}

int main() {
    int result = addNumbers(5, 3);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
