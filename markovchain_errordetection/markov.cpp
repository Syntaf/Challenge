/*
    Markov Chain Error Detection system
*/

#include <iostream>
#include <fstream>
#include <utility>
#include <sstream>

#include <map>

typedef std::map<char, std::map<char, int> > markov_map;

bool readFile(const std::string& filename,  markov_map& data);

int main()
{
    //def table that has 2d length and width of the alphabet
	markov_map markov_chain;
	std::string filename;
	std::string readtmp;
    
    std::cout << "Enter filename: ";
    std::cin >> filename;
    
    if(!readFile(filename, markov_chain)) {
        std::cout << "invalid filename - " << filename << std::endl;
        return -1;
    }

	std::cout << "File read complete...\n" <<
			"Enter the words you would like to check:\n";

	//ignore first newline to prevent getline ending early
	std::cin.ignore();
	std::getline(std::cin, readtmp, '\n');
	readtmp.erase(readtmp.find_last_not_of(" ")+1);
	std::stringstream ss(readtmp);

	std::string word;
	ss >> word;
	while(ss) {
		bool possible_error = false;
		for(int i = 0; i < word.length()-1; i++) {
			if(markov_chain[word[i]][word[i+1]] < 100) {
				std::cout << word << " is likely to have incorrect spelling\n";
				possible_error = true;
				break;
			}
		}
		if(!possible_error)
			std::cout << word << " appears to be spelt correctly\n";
		ss >> word;
	}
	
	return 0;
}

bool readFile(const std::string& filename, markov_map& data)
{
    std::ifstream inFile(filename.c_str());
    if(!inFile.is_open())
        return false;
	std::string readtmp;
	inFile >> readtmp;
	while(inFile) {
		for(int i = 0; i < readtmp.length() - 1; i++) {
			data[readtmp[i]][readtmp[i+1]]++;	
		}
		inFile >> readtmp;
	}
	return true;
}
