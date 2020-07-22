#include "raylib.h"
#include "Level.h"

// std::vector<std::vector<int> > missed_jumps;
// std::vector<Vector2> round_positions;

struct player {
    float x, y;
    int startX, startY;
    int width = 32;
    int height = 32;
    float speedX = 0;
    float speedY = 0;
    float gravity;
    int maxVelY = 15;
    int maxVelX = 5;
    Level& level;
    player(float gravity, Level& a_level, int startX, int startY) : level(a_level) {
        // this->level = level;
        this->gravity = gravity;
        this->startX = startX;
        this->startY = startY;
        x = startX;
        y = startY;
    }
    void update() {
        if (speedY < 0) {
            speedY += gravity * 1.5;
        } else {
            speedY += gravity;
        }
        y += speedY;
        if (speedY > maxVelY) {
            speedY = maxVelY;
        }

        if (speedY < 0) {
            while (level.checkCollision(this->x, this->y, 32)      ||
                   level.checkCollision(this->x + 31, this->y, 32)) {
                y++;
                speedY = 0;
            }
        } else if (speedY > 0) {
            while (level.checkCollision(this->x, this->y + 31, 32)      ||
                   level.checkCollision(this->x + 31, this->y + 31, 32)) {
                y--;
                speedY = 0;
            }
        }

        x += speedX;

        if (speedX < 0) {
            while (level.checkCollision(this->x, this->y, 32)      ||
                   level.checkCollision(this->x, this->y + 31, 32)) {
                x++;
                speedX = 0;
            }
        } else if (speedX > 0) {
            while (level.checkCollision(this->x + 31, this->y, 32)      ||
                   level.checkCollision(this->x + 31, this->y + 31, 32)) {
                x--;
                speedX = 0;
            }
        }
    }
    void jump() {
        if (level.checkCollision(x, y + height, 32)      ||
            level.checkCollision(x + 31, y + height, 32)) {
            speedY = -10;
        } else if (level.checkCollision(x - 1, y + 20, 32)) {
            speedY = -10;
            speedX = 5;
        } else if (level.checkCollision(x + 32, y + 20, 32)) {
            speedY = -10;
            speedX = -5;
        }
        // std::cout << x << ", " << y << std::endl;
    }
    bool checkNum(int num) {
        if (level.checkCollision(x, y, 32)           == num ||
            level.checkCollision(x + 31, y, 32)      == num ||
            level.checkCollision(x, y + 31, 32)      == num ||
            level.checkCollision(x + 31, y + 31, 32) == num) {
                return true;
        }
        return false;
    }
};

void die(player& p, Level& lvl) {
    p.x = p.startX;
    p.y = p.startY;
    p.speedX = 10;
    p.speedY = -7;
    p.level = lvl;
}

int main(int argc, char* argv[])
{
    bool a = true;
    bool b = false;
    bool c[256] = {true};
    std::cout << sizeof(a) << ", " << sizeof(b) << ", " << sizeof(true) << ", " << sizeof(false) << ", " << sizeof(c) << std::endl;

    int screenWidth = 1024;
    int screenHeight = 768;

    InitWindow(screenWidth, screenHeight, "MvsL ReCoded");
    SetTargetFPS(60);

    Texture2D tiles[19] = {
        LoadTexture("tiles/Grass_0.png"),
        LoadTexture("tiles/Grass_1.png"),
        LoadTexture("tiles/Grass_2.png"),
        LoadTexture("tiles/Grass_3.png"),
        LoadTexture("tiles/Grass_4.png"),
        LoadTexture("tiles/Grass_5.png"),
        LoadTexture("tiles/Grass_6.png"),
        LoadTexture("tiles/Grass_7.png"),
        LoadTexture("tiles/Grass_8.png"),
        LoadTexture("tiles/Grass_9.png"),
        LoadTexture("tiles/Grass_10.png"),
        LoadTexture("tiles/Grass_11.png"),
        LoadTexture("tiles/Grass_12.png"),
        LoadTexture("tiles/Pipe_1.png"),
        LoadTexture("tiles/Pipe_2.png"),
        LoadTexture("tiles/Pipe_3.png"),
        LoadTexture("tiles/Pipe_4.png"),
        LoadTexture("tiles/Stone.png"),
        LoadTexture("tiles/barrier.png")
    };
    std::cout << "s1" << std::endl;

    const char* levels[10] = {
        "levels/Slopes.lvl",
        "levels/1-2.lvl",
        "levels/1-3.lvl",
        "levels/1-4.lvl",
        "levels/1-5.lvl",
        "levels/2-1.lvl",
        "levels/2-2.lvl",
        "levels/2-3.lvl",
        "levels/2-4.lvl",
        "levels/2-5.lvl"
    };

    std::cout << "s2" << std::endl;

    short levelnum = 0;
    
    std::cout << levels[levelnum];

    Level debug_lvl = Level(levels[levelnum]);

    std::cout << "s3" << std::endl;

    player p1 = player(0.3f, debug_lvl, debug_lvl.startX1, debug_lvl.startY1);
    player p2 = player(0.3f, debug_lvl, debug_lvl.startX2, debug_lvl.startY2);
    std::cout << "s4" << std::endl;
    die(p1, debug_lvl);
    die(p2, debug_lvl);

    std::cout << "s4" << std::endl;

    int offX = 0;
    int offY = 0;
    int offXmax = debug_lvl.width * 32 - screenWidth;
    int offYmax = debug_lvl.height * 32 - screenHeight;
    int num;

    while (!WindowShouldClose())
    {
        if (IsKeyPressed(KEY_SPACE)) {
            p1.jump();
        }

        if (IsKeyPressed(KEY_O)) {
            p2.jump();
        }

        if (IsKeyDown(KEY_RIGHT)) {
            p1.speedX += 1;
            if (p1.speedX > p1.maxVelX) {
                p1.speedX = p1.maxVelX;
            }
        }

        if (IsKeyDown(KEY_D)) {
            p2.speedX += 1;
            if (p2.speedX > p2.maxVelX) {
                p2.speedX = p2.maxVelX;
            }
        }

        if (IsKeyDown(KEY_LEFT)) {
            p1.speedX -= 1;
            if (p1.speedX < -p1.maxVelX) {
                p1.speedX = -p1.maxVelX;
            }
        }

        if (IsKeyDown(KEY_A)) {
            p2.speedX -= 1;
            if (p2.speedX < -p2.maxVelX) {
                p2.speedX = -p2.maxVelX;
            }
        }

        if (IsKeyDown(KEY_SEMICOLON)) {
            offY++;
        }

        if (!IsKeyDown(KEY_RIGHT) && !IsKeyDown(KEY_LEFT)) {
            if (p1.speedX < 0) {
                p1.speedX += 0.5;
            } else if (p1.speedX > 0) {
                p1.speedX -= 0.5;
            }
            if (p1.speedX < 0.5 && -0.5 < p1.speedX) {
                p1.speedX = 0;
            }
        }

        if (!IsKeyDown(KEY_A) && !IsKeyDown(KEY_D)) {
            if (p2.speedX < 0) {
                p2.speedX += 0.5;
            } else if (p2.speedX > 0) {
                p2.speedX -= 0.5;
            }
            if (p2.speedX < 0.5 && -0.5 < p2.speedX) {
                p2.speedX = 0;
            }
        }

        if (IsKeyPressed(KEY_R)) {
            debug_lvl = Level("levels/Slopes.lvl");
            p1.level = debug_lvl;
            die(p1, debug_lvl);
        }
        
        if (IsKeyPressed(KEY_T)) {
            die(p1, debug_lvl);
        }

        if (IsKeyPressed(KEY_I)) {
            std::cout << GetWindowPosition().x << ", " << GetWindowPosition().y << std::endl;
        }

        // Update the camera
        while (p1.x - offX > 768 && offX < offXmax) {
            offX++;
        }
        while (p1.x - offX < 256 && offX > 0) {
            offX--;
        }

        while (p1.y - offY > 512 && offY < offYmax) {
            offY++;
        }
        while (p1.y - offY < 256 && offY > 0) {
            offY--;
        }


        if (p1.y - offY > 768) {
            die(p1, debug_lvl);
        }


        BeginDrawing();
        ClearBackground(RAYWHITE);

        for (int y = 0; y < (offY % 32 ? 25 : 24); y++) {
            for (int x = 0; x < (offX % 32 ? 33 : 32); x++) {
                num = p1.level.checkCollision(x * 32 + offX, y * 32 + offY, 32);
                if (num > 0) {
                    DrawTextureEx(tiles[num - 1], {(x + offX / 32) * 32 - offX, (y + offY / 32) * 32 - offY}, 0.0f, 2.0f, WHITE);
                }
            }
        }

        p1.update();
        p2.update();
        DrawRectangle(p1.x - offX, p1.y - offY, p1.width, p1.height, GREEN);
        DrawRectangle(p2.x - offX, p2.y - offY, p2.width, p2.height, SKYBLUE);
        DrawFPS(10, 10);
        EndDrawing();
    }

    CloseWindow();

    return 0;
}