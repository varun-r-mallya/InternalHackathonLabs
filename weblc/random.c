#include <emscripten/emscripten.h>
#include <stdlib.h>
#include <string.h>

EMSCRIPTEN_KEEPALIVE 

const char* idk(const char* h) {
    static char result[256];
    strcpy(result, "percy");
    strcat(result, h);
    return result;
}