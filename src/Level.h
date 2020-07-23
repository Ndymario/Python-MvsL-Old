#include <fstream>
#include <iterator>
#include <vector>
#include <iostream>

int get_byte_val(std::vector<unsigned short>& byte_arr, int index);

struct Level {
    std::vector<unsigned short> lvl_raw;
    std::vector<std::vector<unsigned short> > lvl_cmap;
    short width;
    short height;
    int startX1, startY1;
    int startX2, startY2;
    Level(const char* lvl_name);
    unsigned short checkCollision(int x, int y, int scale);
    void changeCollision(int x, int y, int scale, int id);
};