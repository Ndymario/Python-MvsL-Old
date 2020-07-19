#include <fstream>
#include <iterator>
#include <vector>
#include <iostream>
#include "raylib.h"

int get_byte_val(std::vector<unsigned short>& byte_arr, int index);

class Level {
public:
    std::vector<unsigned short> lvl_raw;
    std::vector<std::vector<unsigned short> > lvl_cmap;
    short width;
    short height;
    int startX;
    int startY;
    Level(const char* lvl_name);
    unsigned short checkCollision(int x, int y, int scale);
    void changeCollision(int x, int y, int scale, int id);
};