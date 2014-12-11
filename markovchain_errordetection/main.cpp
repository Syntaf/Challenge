/*
    Markov Chain Error Detection system
*/

#include <iostream>
#include <fstream>
#include <utility>
#include <map>

typedef std::map<char, std::map<char, int> > markov_map;

bool readFile(const std::string& filename,  markov_map& data);

int main()
{
    //def table that has 2d length and width of the alphabet
	markov_map markov_chain;
	std::string filename;
    
    std::cout << "Enter filename: ";
    std::cin >> filename;
    
    if(!readFile(filename, markov_chain)) {
        std::cout << "invalid filename - " << filename << std::endl;
        return -1;
    }

	/* print contents of markov_chain
	for(auto i : markov_chain) {
		for(auto h : std::get<1>(i)) {
			std::cout << std::get<0>(i) << "->" << std::get<0>(h) <<
				" " << std::get<1>(h) << std::endl;
		}
	}
	*/

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
