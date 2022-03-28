-- require "libcall_c_from_lua" -- would work if the .so file is in the same
-- directory. I can probably change the load path or something?? Keep in
-- mind that the .so file's name and the module name need to be identical!
-- The module name is specified by the luaopen_... function in the C file.

-- This executes the registering function, so now we can use the exposed
-- functions
l = package.loadlib("./build/libcall_c_from_lua.so", "luaopen_libcall_c_from_lua")()

-- see here
print(l.my_sin(33))

