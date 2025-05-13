#pragma once
#include <SFML/Graphics.hpp>

using namespace sf;

class Player
{
private:
    const float START_SPEED = 200;
    const float START_HEALTH = 100;

    // Where is the player
    Vector2f m_Position;

    // Of course we will need a sprite
    Sprite m_Sprite;

    // And a texture
    // !!Watch this space!!
    Texture m_Texture;

    // What is the screen resolution
    Vector2f m_Resolution;

    // What size is the current arena
    IntRect m_Arena;

    // How big is each tile of the arena
    int m_TileSize;

    // Which directions is the player currently moving in
    bool m_UpPressed;
    bool m_DownPressed;
    bool m_LeftPressed;
    bool m_RightPressed;

    // How much health has the player got?
    int m_Health;
    // What is the maximum health the player can have
    int m_MaxHealth;

    // When was the player last hit
    Time m_LastHit;

    // Speed in pixels per second
    float m_Speed;

    // All our public functions will come next

public:
    Player();
    void spawn(IntRect, Vector2f, int);
    FloatRect getPosition();
    Vector2f getCenter();
    Sprite getSprite();
    void moveLeft();
    void moveRight();
    void moveUp();
    void moveDown();
    void stopLeft();
    void stopRight();
    void stopUp();
    void stopDown();
    void update(float elapsedTime, Vector2i mousePosition);

    bool hit(Time timeHit);
    Time getLastHitTime();
    float getRotation();
    int getHealth();
    void upgradeSpeed();
    void upgradeHealth();
    void increaseHealthLevel(int amount);
};