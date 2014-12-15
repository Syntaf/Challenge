/*
 *  Generate a random space map and correctly navigate through
 *  the terrain
*/
#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>


const int EMPTY=0;
const int ASTEROID=1;
const int GRAVITYWELL=2;

void printMap(const std::vector<std::vector<int> > &space_map);
bool adjacentToWell(const std::vector<std::vector<int> > &mp, 
                    int index,
                    int r,
                    int c);

int main()
{
    srand(time(NULL));

    int dim=0;
    std::cout << "Enter the dimensions of the map([N][N]): ";
    std::cin >> dim;

    //create two dimensional space map
    std::vector<std::vector<int> > space_map(dim);

    //assign each tile to certain space value
    //  gravity well - 10%
    //  asteroid     - 30%
    //  empty space  - 60%
    for(int i = 0; i < dim; i++) {
        for(int j = 0; j < dim; j++) {
            int probability = (rand() % 100) + 1;
            if(probability < 10)
                space_map[i].push_back(GRAVITYWELL);
            else if(probability < 30)
                space_map[i].push_back(ASTEROID);
            else
                space_map[i].push_back(EMPTY);
        }
    }
    std::cout << "passed\n";
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
            else
                std::cout << ". ";
        }
        std::cout << std::endl;
    }
}

bool adjacentToWell(const std::vector<std::vector<int> > &mp, 
                    int index,
                    int r,
                    int c)
{

}
