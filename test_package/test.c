#include <lauxlib.h>
#include <stdio.h>

int
main(int argc, char** argv){
    lua_State* L = luaL_newstate();
    printf("%d",luaL_dostring(L, "x = 47"));
    printf("%d",lua_getglobal(L, "x"));
    lua_Number x = lua_tonumber(L, 1);
    printf("lua says x = %d\n", (int)x);
    lua_close(L);
}