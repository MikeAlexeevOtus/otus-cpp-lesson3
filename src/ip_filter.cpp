#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

const char COLS_DELIM = '\t';
const char ADDR_DELIM = '.';

using IpSplitted = std::vector<uint8_t>;
using IpList = std::vector<IpSplitted>;


void print_addr(const IpSplitted &addr) {
    for(auto it = addr.cbegin(); it != addr.cend(); it++) {
        if (it != addr.cbegin()) {
            // prepend with dot starting from the second byte
            std::cout << ADDR_DELIM;
        }
        std::cout << (int)*it;
    }
    std::cout << std::endl;
}

void print_addr_list(const IpList &ip_list) {
    for (auto it = ip_list.cbegin(); it != ip_list.cend(); it++) {
        print_addr(*it);
    }
}

IpSplitted parse_addr(const std::string &addr_str) {
    IpSplitted parsed_addr;
    std::string::size_type start = 0, stop = 0;

    while(stop != std::string::npos) {
        stop = addr_str.find_first_of(ADDR_DELIM, start);
        std::string part = addr_str.substr(start, stop - start);
        parsed_addr.push_back(std::stoi(part));

        start = stop + 1;
    }

    return parsed_addr;
}


int main() {
    IpList ip_list;

    for(std::string line; std::getline(std::cin, line);) {
        std::string addr = line.substr(0, line.find(COLS_DELIM));
        ip_list.push_back(parse_addr(addr));
    }

    std::sort(ip_list.begin(), ip_list.end(), std::greater<IpSplitted>());

    print_addr_list(ip_list);
}
