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
#include "astar.hpp"


const int EMPTY=0;			//Empty Space
const int ASTEROID=1;		//Asteroid
const int GRAVITYWELL=2;	//Gravity Well
const int ADJTOWELL=3;	    //Area Affected by Gravity Well
const int PATH=4;			//Path to finish
const int WALL=5;			//Map Boarder

void printMap(const std::vector<std::vector<int>> &space_map);
std::vector<std::vector<int>> makeReadyMap(const std::vector<std::vector<int>>& map);

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
            if(probability < 3)
                space_map[i].push_back(GRAVITYWELL);
            else if(probability < 25)
                space_map[i].push_back(ASTEROID);
            else
                space_map[i].push_back(EMPTY);
        }
		space_map[i].push_back(WALL);
    }

	//start and end should always be... start and end
	space_map[1][1] = space_map[dim][dim] = EMPTY;

	//create lower wall
	std::fill_n(back_inserter(space_map[dim+1]), dim+2, WALL);

	//set all tiles adjacent to G to X
	for(int i = 1; i <= dim; i++) {
		for(int j = 1; j <= dim; j++) {
			if(space_map[i][j] == GRAVITYWELL) {
				for(int di = -1; di <= 1; di++) {
					for(int dj = -1; dj <= 1; dj++) { //dj turn the music up
						if(di == 0 && dj == 0)
							continue;
						space_map[i + di][j + dj] = ADJTOWELL;
					}
				}
			}
		}
	}
    std::string route = findPath(1,1,dim,dim,makeReadyMap(space_map));
	if(route == "")
        std::cout << "No possible route found\n";

    if(route.length() > 0) {
        int x = 0;
        int y = 0;
        for(int i = 0; i < route.length(); i++) {
            char c = route[i];
            int j = atoi(&c);
            x = x + dx[j];
            y = y + dy[j];
            space_map[x][y] = PATH;
        }
    }
    printMap(space_map);

    return 0;
}

void printMap(const std::vector<std::vector<int>> &space_map)
{
    for(int r = 1; r <= space_map.size()-2; r++) {
        for(int c = 1; c <= space_map.size()-2; c++) {
			if(r == 1 && c == 1)
				std::cout << "S ";
			else if(r == space_map.size()-2 && c == space_map.size()-2)
				std::cout << "E ";
			else
				switch(space_map[r][c]) {
					case EMPTY:
						std::cout << ". ";
					break;
					case ASTEROID:
						std::cout << "A ";
					break;
					case GRAVITYWELL:
						std::cout << "G ";
					break;
					case ADJTOWELL:
						std::cout << ". ";
					break;
					case PATH:
						std::cout << "O ";
					break;
					default:
						std::cout << "? ";

					}
		}
        std::cout << std::endl;
    }
}

std::vector<std::vector<int>> makeReadyMap(const std::vector<std::vector<int>>& map)
{
    std::vector<std::vector<int>> resmap(map.size());
    for(int r = 0; r < map.size(); r++) {
        for(int c = 0; c < map.size(); c++) {
            if(map[r][c] > 0) {
                resmap[r].push_back(1);
            }else{
                resmap[r].push_back(0);
            }
        }
        std::cout << std::endl;
    }
    return resmap;
}
