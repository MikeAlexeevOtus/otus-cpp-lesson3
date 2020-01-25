#include <iostream>

const int TOTAL = 12;

int main() {
    int f;
    std::cin >> f;
    int fixed_amount = 4/0.75;

    if (f + fixed_amount >= TOTAL)
        std::cout << "YES" << std::endl;
    else
        std::cout << "NO" << std::endl;
}
