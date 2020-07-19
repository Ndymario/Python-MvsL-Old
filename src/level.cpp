#include "Level.h"

int get_byte_val(std::vector<short>& byte_arr, int index) {
    return byte_arr[index] * 256 + byte_arr[index + 1];
}

Level::Level(const char* lvl_name)  {
    std::ifstream input(lvl_name, std::ios::binary);

    std::vector<short> bytes(
        (std::istreambuf_iterator<char>(input)),
        (std::istreambuf_iterator<char>()));

    input.close();

    for (short i = 0; i < bytes.size(); i++) {
        if (bytes[i] < 0) {
            bytes[i] += 256;
        }
    }

    lvl_raw.insert(lvl_raw.end(), bytes.begin(), bytes.end());

    // Constructing the CMap
    for (int y = 0; y < get_byte_val(bytes, 6); y++) {
        lvl_cmap.push_back({});
        for (int x = 0; x < get_byte_val(bytes, 4); x++) {
            lvl_cmap[y].push_back(0);
        }
    }
    int index = 14;
    unsigned short id;
    unsigned short x;
    unsigned short y;
    unsigned short w;
    unsigned short h;
    while (get_byte_val(bytes, index) != 65535) {
        id = get_byte_val(bytes, index);
        index += 2;
        x = get_byte_val(bytes, index);
        index += 2;
        y = get_byte_val(bytes, index);
        index += 2;
        w = get_byte_val(bytes, index);
        index += 2;
        h = get_byte_val(bytes, index);
        index += 2;
        if (id != 19) {
            for (unsigned short posY = 0; posY < h; posY++) {
                for (unsigned short posX = 0; posX < w; posX++) {
                    lvl_cmap[y + posY][x + posX] = id;
                }
            }
        } else {
            startX = x * 16;
            startY = y * 16;
        }
    }
    width = get_byte_val(bytes, 4);
    height = get_byte_val(bytes, 6);
}

unsigned short Level::checkCollision(int x, int y, int scale = 16) {
    x /= scale;
    y /= scale;
    if (x >= lvl_cmap[0].size() || y >= lvl_cmap.size()) {
        return 0;
    }
    return this->lvl_cmap[y][x];
}

void Level::changeCollision(int x, int y, int scale, int id) {
    lvl_cmap[y / scale][x / scale] = id;
}