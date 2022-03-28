#include <lauxlib.h>
#include <lua.h>
#include <math.h>
#include <unistd.h>

void wait_a_second() { sleep(1); }

static int l_sin(lua_State *L) {
    double d = lua_tonumber(L, 1); /* get argument */
    lua_pushnumber(L, sin(d));     /* push result */
    return 1;                      /* number of results */
}

// library to be registered
static const struct luaL_Reg mylib[] = {
    {"my_sin", l_sin}, /* names can be different */
    {NULL, NULL}       /* sentinel */
};

// name of this function is not flexible
int luaopen_libcall_c_from_lua(lua_State *L) {
    luaL_newlib(L, mylib);
    return 1;
}

/* int main() { */

/*     /1* lua_pushcfunction(l, l_sin); *1/ */
/*     /1* lua_setglobal(l, "mysin"); *1/ */
/*     /1* return 0; *1/ */
/* } */
