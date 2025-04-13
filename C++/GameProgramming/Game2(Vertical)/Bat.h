#pragma once
#include <SFML/Graphics.hpp>
using namespace sf;

class Bat{
    Vector2f m_position;
    RectangleShape m_shape;
    float m_speed;
    bool m_moving_left = false;
    bool m_moving_right = false;
    int m_height, m_width;
    Vector2f m_screenSize;
public:
    Bat(int, int, Vector2f); //for bat size only
    Bat(int, int, float, float, Vector2f); //for bat size as well as position
    FloatRect getPosition();
    RectangleShape getShape();
    float getSpeed();
    void setSpeed(float);
    void setShape(RectangleShape);
    void moveLeft();
    void stopLeft();
    void moveRight();
    void stopRight();
    void update(Time);
};