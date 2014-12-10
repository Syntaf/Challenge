/*
    Markov Chain Error Detection system
*/

#include <iostream>
#include <fstream>

bool readFile(const std::string& filename, char markov[][26]);

int main()
{
    //def table that has 2d length and width of the alphabet
    char markov_table[26][26];
    std::string filename;
    
    std::cout << "Enter filename: ";
    std::cin >> filename;
    
    if(!readFile(filename, markov_table)) {
        std::cout << "invalid filename - " << filename << std::endl;
        return -1;
    }


}

bool readFile(const std::string& filename, char markov[][26])
{
    std::ifstream inFile(filename.c_str());
    if(!inFile.is_open())
        return false;
}
