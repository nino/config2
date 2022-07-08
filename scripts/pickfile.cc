#include <cstdlib>
#include <ctime>
#include <filesystem>
#include <iostream>
#include <vector>

namespace fs = std::filesystem;

std::vector<std::string> files_in_dir(std::string dir);

std::vector<std::string> files_in_dir(std::string dir) {
    std::vector<std::string> entries;
    for (const auto& entry : fs::directory_iterator(dir)) {
        if (entry.is_directory()) {
            std::vector<std::string> children = files_in_dir(entry.path());
            for (const std::string path : children) {
                entries.push_back(path);
            }
        }
        entries.push_back(entry.path());
    }
    return entries;
}

std::string random_file_in_dir(std::string dir) {
    /* std::vector<std::string> entries; */
    /* for (const auto& entry : fs::directory_iterator(path)) { */
    /*     entries.push_back(entry.path()); */
    /* } */
    std::vector<std::string> entries = files_in_dir(dir);
    int rand_index = rand() % entries.size();
    return entries[rand_index];
}

int main(int argc, char** argv) {
    srand(time(NULL));

    std::string path = ".";
    if (argc == 2) {
        path = argv[1];
    }

    /* std::vector<std::string> entries; */
    /* for (const auto& entry : fs::directory_iterator(path)) { */
    /*     entries.push_back(entry.path()); */
    /* } */

    std::cout << random_file_in_dir(path) << std::endl;

    /* int rand_index = rand() % entries.size(); */
    /* std::cout << entries[rand_index] << std::endl; */
}
