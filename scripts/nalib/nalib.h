#pragma once

#include <stdio.h>

#pragma mark Headers

typedef enum FILE_READ_RESULT {
    FR_SUCCESS,
    FR_FAILED_TO_OPEN,
    FR_FAILED_TO_ALLOCATE_RESULT,
} FILE_READ_RESULT;

/**
 * Read complete contents of a file. Allocates memory to the `result` parameter
 * using the `allocate` parameter.
 *
 * `allocate` should take a number of bytes.
 */
FILE_READ_RESULT readfile(const char* path,
                          void* allocate(size_t),
                          char** result);

#define sliceof(Type) \
    struct {          \
        T* arr;       \
        size_t len;   \
    }

struct voidslice {
    void* arr;
    size_t len;
};

#ifdef NALIB_IMPLEMENTATION
#undef NALIB_IMPLEMENTATION

#pragma mark Implementation

FILE_READ_RESULT
readfile(const char* path, void* allocate(size_t), char** result) {
    FILE* fp = fopen(path, "r");
    if (fp == NULL) {
        return FR_FAILED_TO_OPEN;
    }

    fseek(fp, 0, SEEK_END);
    int filesize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    *result = allocate(filesize * sizeof(char));
    if (*result == NULL) {
        return FR_FAILED_TO_ALLOCATE_RESULT;
    }
    fread(*result, sizeof(char), filesize, fp);

    fclose(fp);

    return FR_SUCCESS;
}

#endif
