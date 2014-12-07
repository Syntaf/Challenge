#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

typedef std::vector<std::string> vec;

vec openDictionary(std::ifstream& fileIn, std::string fName = "data.dat");
std::string parse(vec& d, std::string in);
bool is_number(const std::string& s);
bool is_punct(const std::string& s);

int main()
{
	//we want to declare one ifstream to read the file in seperate functions
	std::ifstream dataFile;
	auto dict = openDictionary(dataFile);
	
	//unpack data and read commands
	std::string command;
	while(dataFile >> command) {
		if(is_number(command)){			//print word normally
			std::cout << dict.at(atoi(command.c_str())) << " ";
		}else if(command == "-"){		//hypen following words
			std::cout << '\b' << "-";
		}else if(is_punct(command)){		//add to end of word
			std::cout << '\b' << command << " ";
		}else if(command == "R"){		//print new line
			std::cout << "\n";
		}else if(command == "E"){		//end unpacking
			break;
		}else{					//special cases
			std::cout << parse(dict, command) << " ";	
		}
	}
}

vec openDictionary(std::ifstream& fileIn, std::string fName)
{
	vec temp;
	fileIn.open(fName.c_str());
	if(!fileIn.is_open()){
		std::cerr << "Unable to open " << fName << ".dat ...\n";
		return temp;
	}
	int size;
	std::string read;
	//find how many values we need to loop for the dictionary
	fileIn >> size; 
	//loop while i is below size, and our file is not at EOF(2 conditions)
	for(auto i =0; i < size; i++) {
		fileIn >> read;
		//push value back into our vector
		temp.push_back(read);
	}
	//return finished vector
	return temp;
}

std::string parse(vec& d, std::string in)
{
	//return string
	std::string result;
	//stores the index of the given word
	std::string key = "";
	//loop through string
	for(auto i=0; i < in.size(); i++) {	
		if(std::isdigit(in[i])){
			key = key + in[i];
		}else{
			std::string str = d.at(atoi(key.c_str()));
			if(in[i] == '^'){
				str[0] = std::toupper(str[0]);
				return str;
			}
			else if(in[i] == '!'){
				std::transform(begin(str),end(str),begin(str),::toupper);
				return str;
			}
		}
	}
	return "invalid file input: " + in;
}

bool is_number(const std::string& s)
{
	return !s.empty() && std::find_if(
			begin(s), 
			end(s), 
			[](char c) {return !std::isdigit(c); }) == end(s);
}

bool is_punct(const std::string& s)
{
	return !s.empty() && std::find_if(
			begin(s),
			end(s),
			[](char c) {return !std::ispunct(c); }) == end(s);
}

