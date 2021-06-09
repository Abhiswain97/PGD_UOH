#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <cmath>
#include <sstream>

int main(int argc, char const *argv[])
{
    std::vector<std::string> corpus = {
        "This is the first document mostly",
        "This document is the second document",
        "And this is the third one",
        "Is this the first document here",
    };

    std::vector<std::vector<std::string>> word_list;

    std::string tokens;

    for (std::string s : corpus)
    {
        std::vector<std::string> temp;

        std::stringstream sen(s);
        std::string intermediate;

        while (std::getline(sen, intermediate, ' '))
        {
            std::cout << intermediate << std::endl;

            temp.push_back(intermediate);
        }
        word_list.push_back(temp);
    }

    for (auto &sen : word_list)
    {
        std::cout << sen.size() << std::endl;
    }

    return 0;
}
