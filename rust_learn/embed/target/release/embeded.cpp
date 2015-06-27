#include <iostream>
#include <stdlib.h>
#include <dlfcn.h>

int main() 
{
    void *handle;
    std::cout << "Using libembed.so" << std::endl;
    handle = dlopen("./libembed.so", RTLD_LAZY);
    if(!handle) {
        std::cout << "Error... " << dlerror() << std::endl;
        dlerror();
    }
    dlerror();
    dlsym(handle, "process");
    char *error = dlerror();
    if(error != NULL) {
        std::cout << "error: " << error << std::endl;
    }
    dlclose(handle);

    std::cout << "Done" << std::endl;
}
