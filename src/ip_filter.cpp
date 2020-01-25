#include <algorithm>
#include <functional>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

const char COLS_DELIM = '\t';
const char ADDR_DELIM = '.';

using IpByte = uint8_t;
using IpAddr = std::vector<IpByte>;
using IpList = std::vector<IpAddr>;


void print_addr(const IpAddr &addr) {
    for(auto it = addr.cbegin(); it != addr.cend(); it++) {
        if (it != addr.cbegin()) {
            // prepend with dot starting from the second byte
            std::cout << ADDR_DELIM;
        }
        std::cout << (int)*it;
    }
    std::cout << std::endl;
}

void print_addr_list(const IpList &ip_list,
                     std::function<bool(const IpAddr&)> test_function) {
    for (auto it = ip_list.cbegin(); it != ip_list.cend(); it++) {
        if (test_function(*it))
            print_addr(*it);
    }
}

void print_addr_list(const IpList &ip_list) {
    for (auto it = ip_list.cbegin(); it != ip_list.cend(); it++) {
        print_addr(*it);
    }
}

IpAddr parse_addr(const std::string &addr_str) {
    IpAddr parsed_addr;
    std::string::size_type start = 0, stop = 0;

    while(stop != std::string::npos) {
        stop = addr_str.find_first_of(ADDR_DELIM, start);
        std::string part = addr_str.substr(start, stop - start);
        parsed_addr.push_back(std::stoi(part));

        start = stop + 1;
    }

    return parsed_addr;
}


bool any_is_equal(const IpAddr &ip_addr, IpByte value) {
    return std::any_of(
            ip_addr.cbegin(),
            ip_addr.cend(),
            [value](IpByte ip_byte) { return ip_byte == value; }
        );
}


int main() {
    IpList ip_list;

    for(std::string line; std::getline(std::cin, line);) {
        // cut first column
        std::string addr = line.substr(0, line.find(COLS_DELIM));
        ip_list.push_back(parse_addr(addr));
    }

    std::sort(ip_list.begin(), ip_list.end(), std::greater<IpAddr>());

    print_addr_list(ip_list);
    print_addr_list(ip_list, [](const IpAddr &ip_addr) { return ip_addr[0] == 1; });
    print_addr_list(ip_list, [](const IpAddr &ip_addr) { return ip_addr[0] == 46 && ip_addr[1] == 70; });
    print_addr_list(ip_list, [](const IpAddr &ip_addr) { return any_is_equal(ip_addr, 46); });
}
