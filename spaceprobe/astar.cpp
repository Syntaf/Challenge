//astar.cpp
#include <iostream>
#include <iomanip>
#include <queue>
#include <string>
#include <math.h>
#include <ctime>

class node
{
	public:
        node(int xp, int yp, int d, int p):
            xPos(xp),yPos(yp),level(d),priority(p){}

        int getxPos() const {return xPos;}
        int getyPos() const {return yPos;}
        int getLevel() const {return level;}
        int getPriority() const {return priority;}

        void updatePriority(const int &xDest, const int &yDest)
        {
            priority = level+estimate(xDest, yDest)*10;
        }

        void nextLevel(const int &i)
        {
            level += i%2 == 0?10:14;
        }

        const int &estimate(const int &xDest, const int &yDest)
        {
            static int xd, yd, d;
            xd = xDest - xPos;
            yd = yDest - yPos;

            d = (int)(sqrt(xd * xd + yd * yd));

            return d;
        }
	private:
		//x and y pos
		int xPos;
		int yPos;
		//total distanced traveled
		int level;
		//level + remaining distance estimate
		int priority;

};

bool operator<(const node &a, const node &b)
{
    return a.getPriority() > b.getPriority();
}

string findPath( const int &xStart, const int &yStart,
                 const int xFinish, const int &yFinish,
                 std::vector< std::vector<int> > map)
{
    n = map.size()-2;
    static int closed_nodes_map[n][n];
    static int open_nodes_map[n][n];
    static int dir_map[n][n];
    static int dir=8;
    static int ix[dir] = {1,1,0,-1,-1,0,1};
    static int dy[dir] = {0,1,1,1,0,-1,-1,-1};

    static std::priority_queue<node> pq[2];
    static int pqi=0;
    static node* n0;
    static node* m0;
    static int i, j, x, y, xdx, ydy;
    static char c;
    
    for(y = 0; y < n; y++) {
        for(x = 0; x < n; x++) {
            closed_nodes_map[x][y] = 0;
            open_nodes_map[x][y] = 0;
        }
    }

    n0 = new node(xStart, yStart, 0, 0);
    n0->updatePriority(xFinish, yFinish);
    pq[pqi].push(*n0);
    open_nodes_map[x][y]=n0->getPriority();

    while(!pq[pqi].empty()) {
        n0 = new node( pq[pqi].top().getxPos(), pq[pqi].top().getyPos(),
                       pq[pqi].top().getLevel(), pq[pqi].top().getPriority());
        
        x = n0->getxPos();
        y = n0->getyPos();
        
        pq[pqi].pop();
        open_nodes_map[x][y] = 0;
        closed_nodes_map[x][y] = 1;

        if(x == xFinish && y == yFinish) {
            std::string path="";
            while(!(x == xStart && y = yStart)) {
                j = dir_map[x][y];
                c = '0'+(j+dir/2)%dir;
                path = c + path;
                x += dx[j];
                y += dy[j];
            }

            delete n0;
            while(!pq[pqi].empty())
                pq[pqi].pop();
            return path;
        }

        for(i = 0; i < dir; i++) {
            xdx = x + dx[i];
            ydy = y + dy[i];

            if(!(xdx < 0 || xdx > n-1 || ydy < 0 || ydy > n-1 || map[xdx][ydy] == 1
                         || closed_nodes_map[xdx][ydy] == 1)) {
                m0 = new node( xdx, ydy, n0->getLevel(),
                        n0->getPriority());
                m0->nextLevel(i);
                m0->updatePriority(xFinish, yFinish);

                if(open_nodes_map[xdx][ydy] == 0) {
                    open_nodes_map[xdx][ydy] = m0->getPriority();
                    pq[pqi].push(m0*);
                    dir_map[xdx][ydy]=(i+dir/2)%dir;
                }else if(open_nodes_map[xdx][ydy] > m0->getPriority()) {
                    open_nodes_map[xdx][ydy] = m0->getPriority();
                    dir_map[xdx][ydy] = (i+dir/2)%dir;

                    while(!(pq[pqi].top().getxPos() == xdx &&
                           pq[pqi].top().getyPos() == ydy)) {
                        pq[1-pqi].push(pq[pqi].top());
                        pq[pqi].pop();
                    }
                    pq[pqi].pop();

                    if(pq[pqi].size() > pq[1-pqi].size())
                        pqi = 1 - pqi;

                    while(!pq[pqi].empty()) {
                        pq[1-pqi].push(pq[pqi].top());
                        pq[pqi].pop();
                    }
                    pqi=1-pqi;
                    pq[pqi].push(*m0);
                }
                else delete m0;
            }
        }
        delete n0;
    }
    return "";
}
   













