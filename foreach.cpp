#include <iostream>

template<typename tFunc, typename... tArgs>
void forArgs(tFunc && mFunc, tArgs&&... mArgs)
{
    return (void) std::initializer_list<int> 
    {
        (
            mFunc(std::forward<tArgs>(mArgs)), 0
        )...
    };
}

int main()
{
    forArgs(
        [](const auto& x){ std::cout << x << std::endl; },
        "hello",
        1,
        2,
        3
    );

    return 0;
}
