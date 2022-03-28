#include <stdio.h>
#include <stdlib.h>

#define NALIB_IMPLEMENTATION
#include "nalib/nalib.h"

int main() { 
  char* file_contents;
  readfile("sql-copy", malloc, &file_contents);
  puts(file_contents);
}
