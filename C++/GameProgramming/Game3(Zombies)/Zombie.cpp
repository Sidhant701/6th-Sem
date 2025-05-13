#include "Zombie.h"
#include <cmath>
bool Zombie::hit()
{
    m_Health--;
    if (m_Health < 0)
    {
        // Dead
        m_Alive = false;
        m_texture.loadFromFile("graphics/blood.png");
        m_Sprite.setTexture(m_texture);
        return true;
    }
    // Injured but not dead
    return false;
}
bool Zombie::isAlive()
{
    return m_Alive;
}
void Zombie::spawn(float startX, float startY, int type, int seed)
{
    switch (type)
    {
    case 0:
        m_texture.loadFromFile("graphics/bloater.png");
        m_Sprite.setTexture(m_texture); // BLOATER
        // m_Sprite.setTexture(TextureHolder::getTexture("graphics/bloater.png")); // Using setTexture
        m_Speed = BLOATER_SPEED;
        m_Health = BLOATER_HEALTH;
        break;
    case 1:
        m_texture.loadFromFile("graphics/chaser.png");
        m_Sprite.setTexture(m_texture); // CHASER
        // m_Sprite = Sprite(TextureHolder::getTexture("graphics/chaser.png")); // Using Constructor instead of setTexture
        m_Speed = CHASER_SPEED;
        m_Health = CHASER_HEALTH;
        break;
    case 2: // CRAWLER
        m_texture.loadFromFile("graphics/crawler.png");
        m_Sprite.setTexture(m_texture);
        // m_Sprite.setTexture(TextureHolder::getTexture("graphics/crawler.png"));
        m_Speed = CRAWLER_SPEED;
        m_Health = CRAWLER_HEALTH;
        break;
    }

    // Modify the speed slightly
    srand((int)time(0) * seed);
    float modifier = (rand() % MAX_VARIANCE) + OFFSET; // modifier is in between 70 and 100
    m_Speed = m_Speed * modifier / 100;                // Speed is now a number between 70% and 100% of the original speed

    m_Alive = true;
    m_Position.x = startX;
    m_Position.y = startY;

    m_Sprite.setOrigin(25, 25);

    m_Sprite.setPosition(m_Position);
}
FloatRect Zombie::getPosition()
{
    return m_Sprite.getGlobalBounds();
}
Sprite Zombie::getSprite()
{
    return m_Sprite;
}
void Zombie::update(float elapsedTime, Vector2f playerPosition)
{
    float playerX = playerPosition.x;
    float playerY = playerPosition.y;

    if (playerX > m_Position.x)
        m_Position.x += m_Speed * elapsedTime;
    if (playerY > m_Position.y)
        m_Position.y += m_Speed * elapsedTime;
    if (playerX < m_Position.x)
        m_Position.x -= m_Speed * elapsedTime;
    if (playerY < m_Position.y)
        m_Position.y -= m_Speed * elapsedTime;
    m_Sprite.setPosition(m_Position);
    float angle = (atan2(playerY - m_Position.y, playerX - m_Position.x) * 180) / 3.141;
    m_Sprite.setRotation(angle);
}