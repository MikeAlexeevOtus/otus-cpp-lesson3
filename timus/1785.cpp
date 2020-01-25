#include <iostream>
#include <vector>
#include <string>

using LocPair = std::pair<int, std::string>;
using LocGrades = std::vector<LocPair>;


LocGrades init_loc_grades() {
    LocGrades loc_grades;

    // lower bound, name
    loc_grades.push_back(LocPair(1, "few"));
    loc_grades.push_back(LocPair(5, "several"));
    loc_grades.push_back(LocPair(10, "pack"));
    loc_grades.push_back(LocPair(20, "lots"));
    loc_grades.push_back(LocPair(50, "horde"));
    loc_grades.push_back(LocPair(100, "throng"));
    loc_grades.push_back(LocPair(250, "swarm"));
    loc_grades.push_back(LocPair(500, "zounds"));
    loc_grades.push_back(LocPair(1000, "legion"));

    return loc_grades;
}


int main() {
    LocGrades loc_grades = init_loc_grades();
    std::string name = loc_grades[0].second;   //default result

    int amount;
    std::cin >> amount;

    for(auto it = loc_grades.cbegin(); it != loc_grades.cend(); it++) {
        if (amount >= it->first)
            name = it->second;
    }
    std::cout << name << std::endl;
}
