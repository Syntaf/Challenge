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


const int EMPTY=0;			//Empty Space
const int ASTEROID=1;		//Asteroid
const int GRAVITYWELL=2;	//Gravity Well
const int ADJTOWELL=3;	    //Area Affected by Gravity Well
const int WALL=4;			//Map Boarder

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
    
    printMap(space_map);

    return 0;
}

void printMap(const std::vector<std::vector<int> > &space_map)
{
    for(int r = 1; r <= space_map.size()-2; r++) {
        for(int c = 1; c <= space_map.size()-2; c++) {
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
					std::cout << "X ";
				break;
				default:
					std::cout << "? ";

			}
		}
        std::cout << std::endl;
    }
}
