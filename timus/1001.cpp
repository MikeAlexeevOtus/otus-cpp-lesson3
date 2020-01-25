#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <math.h>

using VectorD = std::vector<double>;


void read_input(VectorD &input_values) {
    for(std::string line; std::getline(std::cin, line);) {
        double val;
        std::istringstream iss(line);
        while(iss >> val) {
            input_values.push_back(val);
        }
    }
}

int main() {
    VectorD input_values;
    read_input(input_values);

    for (auto it = input_values.crbegin(); it != input_values.crend(); it++) {
        std::cout << std::fixed << std::sqrt(*it) << std::endl;
    }
}
