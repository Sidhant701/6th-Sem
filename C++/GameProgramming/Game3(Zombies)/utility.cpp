#pragma once
#include <SFML/Graphics.hpp>
#include "Zombie.h"
using namespace sf;
int createBackground(VertexArray &rVA, IntRect arena)
{
    const int TILE_SIZE = 50;
    const int TILE_TYPES = 3;
    const int VERTS_IN_QUAD = 4;

    int worldWidth = arena.width / TILE_SIZE;
    int worldHeight = arena.height / TILE_SIZE;

    rVA.setPrimitiveType(Quads);
    rVA.resize(worldWidth * worldHeight * VERTS_IN_QUAD);

    int currentVertex = 0;
    for (int i = 0; i < worldWidth; i++)
    {
        for (int j = 0; j < worldHeight; j++)
        {
            // Position each vertex in the current quad
            rVA[currentVertex + 0].position = Vector2f(i * TILE_SIZE, j * TILE_SIZE);
            rVA[currentVertex + 1].position = Vector2f((i + 1) * TILE_SIZE, j * TILE_SIZE);
            rVA[currentVertex + 2].position = Vector2f((i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE);
            rVA[currentVertex + 3].position = Vector2f(i * TILE_SIZE, (j + 1) * TILE_SIZE);

            // Define the position in the Texture to draw for current quad
            // Either mud, stone, grass or wall
            if (j == 0 || j == (worldHeight - 1) || i == 0 || i == (worldWidth - 1))
            {
                // Use the wall texture
                rVA[currentVertex + 0].texCoords = Vector2f(0, 0 + TILE_TYPES * TILE_SIZE);
                rVA[currentVertex + 1].texCoords = Vector2f(TILE_SIZE, 0 + TILE_TYPES * TILE_SIZE);
                rVA[currentVertex + 2].texCoords = Vector2f(TILE_SIZE, TILE_SIZE + TILE_TYPES * TILE_SIZE);
                rVA[currentVertex + 3].texCoords = Vector2f(0, TILE_SIZE + TILE_TYPES * TILE_SIZE);
            }
            else
            {
                // Use a random floor texture
                srand((int)time(0) + j * i - j);
                int mOrG = (rand() % TILE_TYPES);
                int verticalOffset = mOrG * TILE_SIZE;

                rVA[currentVertex + 0].texCoords = Vector2f(0, 0 + verticalOffset);
                rVA[currentVertex + 1].texCoords = Vector2f(TILE_SIZE, 0 + verticalOffset);
                rVA[currentVertex + 2].texCoords = Vector2f(TILE_SIZE, TILE_SIZE + verticalOffset);
                rVA[currentVertex + 3].texCoords = Vector2f(0, TILE_SIZE + verticalOffset);
            }

            currentVertex = currentVertex + VERTS_IN_QUAD;
        }
    }

    return TILE_SIZE;
}

Zombie *createHorde(int numZombies, IntRect arena)
{
    Zombie *zombies = new Zombie[numZombies];
    int maxY = arena.height - 20;
    int minY = arena.top + 20;
    int maxX = arena.width - 20;
    int minX = arena.left + 20;

    for (int i = 0; i < numZombies; i++)
    {
        srand((int)time(0) * i);
        int side = (rand() % 4);
        float x, y;
        switch (side)
        {
        case 0: // left
            x = minX;
            y = (rand() % maxY) + minY;
            break;
        case 1: // right
            x = maxX;
            y = (rand() % maxY) + minY;
            break;
        case 2: // top
            x = (rand() % maxX) + minX;
            y = minY;
            break;
        case 3: // bottom
            x = (rand() % maxX) + minX;
            y = maxY;
            break;
        }

        // Bloater, runner or crawler
        srand((int)time(0) * i * 2);
        int type = (rand() % 3);

        // Spawn the zombie into the array
        zombies[i].spawn(x, y, type, i);
    }

    return zombies;
}