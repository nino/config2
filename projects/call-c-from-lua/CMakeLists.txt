cmake_minimum_required(VERSION 3.22)
project(call_c_from_lua)

set(SOURCE_FILES lib.c)

find_package(Lua 5.1 REQUIRED)
# set(LUA_PREFERRED_INCLUDE_DIRS ${LUA_INCLUDE_DIR})
# set(LUA_PREFERRED_LIBRARIES ${LUA_LIBRARIES})
set(CMAKE_EXPORT_COMPILE_COMMANDS on)

include_directories(/usr/local/include ${LUA_INCLUDE_DIR})

add_library(call_c_from_lua SHARED ${SOURCE_FILES})
SET_TARGET_PROPERTIES(call_c_from_lua PROPERTIES SUFFIX .so)

target_link_libraries(call_c_from_lua ${LUA_LIBRARIES})
