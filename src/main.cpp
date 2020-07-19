#include "level.h"

using namespace std;


void EPIC_NAME(float x,float y, Texture2D& wow, Rectangle& wow_1);

int main(int argc, char* argv[])
{
    // Initialization
    //--------------------------------------------------------------------------------------
    int screenWidth = 256;
    int screenHeight = 192;
    int x = 32;
    int y = 32;
    int key;
    Level level = Level("Levels/1-1.lvl");

    InitWindow(screenWidth, screenHeight, "raylib [core] example - basic window");
    Texture2D Mario = {
        LoadTexture("Sprites/Mario/small.png")
    };
    Rectangle mario_1 = {2,2,14,22};
    Rectangle def_tile = {0,0,16,16};
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
    SetTargetFPS(144);
    //--------------------------------------------------------------------------------------
    

    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // Update
        //----------------------------------------------------------------------------------
        
        if (IsKeyDown (KEY_A)) {
            x -= 2;
        }
        if (IsKeyDown (KEY_D)) {
            x += 2;
        }
        if (IsKeyDown (KEY_W)) {
            if (y >= 160) {
                y -= 50;
            }
        }
        if (y > 160) {
            y = 168;
        } else {
            y += 2;
        }
        
        
        
        // TODO: Update your variables here
        //----------------------------------------------------------------------------------
        
        // Draw
        //----------------------------------------------------------------------------------
        BeginDrawing();

        ClearBackground(RAYWHITE);
        
        for (int ty = 0; ty < 12; ty++) {
                for (int tx = 0; tx < 16; tx++) {
                    int number = level.checkCollision(tx,ty,1);
                    if (number != 0) {
                        DrawTextureRec(tiles[number-1], def_tile,{tx * 16, ty * 16},WHITE);
                    }
                }
        }
        DrawTextureRec(Mario,mario_1,{x,y},WHITE);
        EndDrawing();

        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------   
    CloseWindow();        // Close window and OpenGL context
    //--------------------------------------------------------------------------------------

    return 0;
}



