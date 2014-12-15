/*
 *  Generate a random space map and correctly navigate through
 *  the terrain
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <ctime>
#include <cstdlib>


const int EMPTY=0;
const int ASTEROID=1;
const int GRAVITYWELL=2;
const int WALL=3;

void printMap(const std::vector<std::vector<int> > &space_map);

int main()
{
    srand(time(NULL));

    int dim=0;
    std::cout << "Enter the dimensions of the map([N][N]): ";
    std::cin >> dim;
    std::vector<std::vector<int> > space_map(dim+2);

	//create upper wall
	std::fill_n(back_inserter(space_map[0]), dim+2, WALL);

    //assign each tile to certain space value
    //  gravity well - 10%
    //  asteroid     - 30%
    //  empty space  - 60%
    for(int i = 1; i < dim+1; i++) {
		space_map[i].push_back(WALL);
        for(int j = 1; j < dim+1; j++) {
            int probability = (rand() % 100) + 1;
            if(probability < 10)
                space_map[i].push_back(GRAVITYWELL);
            else if(probability < 30)
                space_map[i].push_back(ASTEROID);
            else
                space_map[i].push_back(EMPTY);
        }
		space_map[i].push_back(WALL);
    }

	//create lower wall
	std::fill_n(back_inserter(space_map[dim+1]), dim+2, WALL);
    
    printMap(space_map);

    return 0;
}

void printMap(const std::vector<std::vector<int> > &space_map)
{
    for(int r = 0; r < space_map.size(); r++) {
        for(int c = 0; c < space_map.size(); c++) {
            if(space_map[r][c] == ASTEROID)
                std::cout << "A ";
            else if(space_map[r][c] == GRAVITYWELL)
                std::cout << "G ";
            else if(adjacentToWell(space_map, space_map[r][c],r,c))
                std::cout << "X ";
            else if(c > 0)
        		std::cout << ".";
		}
        std::cout << std::endl;
    }
}
