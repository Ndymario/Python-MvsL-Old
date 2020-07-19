#include "raylib.h"
#include <iostream>
#include <vector>

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
    
    InitWindow(screenWidth, screenHeight, "raylib [core] example - basic window");
    Texture2D Mario = {
        LoadTexture("Sprites/Mario/small.png")
    };
    Rectangle mario_1 = {2,2,14,22};
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
        EPIC_NAME(x,y, Mario, mario_1);
        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------   
    CloseWindow();        // Close window and OpenGL context
    //--------------------------------------------------------------------------------------

    return 0;
}

void EPIC_NAME(float x,float y, Texture2D& wow, Rectangle& wow_1) {
    BeginDrawing();   
        ClearBackground(RAYWHITE);
        DrawText("h", 190, 100, 20, LIGHTGRAY);
        DrawTextureRec(wow,wow_1,{x,y},WHITE);
    EndDrawing();
}