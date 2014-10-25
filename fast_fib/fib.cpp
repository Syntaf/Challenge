#include <iostream>
#include <algorithm>

/* 
 * converted C fib algorithm to compile
 * and take advantage of c++ concepts
 * runetime should be O(log N)
*/
long long fibonacci(int n)
{
  long long fib[2][2] = {{1,1},{1,0}},
            ret[2][2] = {{1,0},{0,1}},
            tmp[2][2] = {{0,0},{0,0}};
  while(n) {
    if(n&1) {
      std::fill(&tmp[0][0], &tmp[0][0] + 4, 0);
      for(int i = 0; i < 2; i++)
        for(int j = 0; j < 2; j++)
          for(int k = 0; k < 2; k++)
            tmp[i][j] = ( tmp[i][j] + ret[i][k] * fib[k][j] );
      for(int i = 0; i < 2; i++)
        for(int j = 0; j < 2; j++)
          ret[i][j] = tmp[i][j];
    }
    std::fill(&tmp[0][0], &tmp[0][0] + 4, 0);
    for(int i = 0; i < 2; i++)
      for(int j = 0; j < 2; j++)
        for(int k = 0; k < 2; k++)
          tmp[i][j] = ( tmp[i][j] + fib[i][k] * fib[k][j] );
    for(int i = 0; i < 2; i++)
      for(int j = 0; j < 2; j++)
        fib[i][j] = tmp[i][j];
    n/=2;
  }
  return (ret[0][1]);
}

int main(int argc, char* argv[])
{
  int param = atoi(argv[1]);
  while(param > 0) {
    std::cout << fibonacci(param) << ", ";
    param--;
  }
  return 0;
}
