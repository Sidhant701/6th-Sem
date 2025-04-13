#pragma once
#include <SFML/Graphics.hpp>
using namespace sf;


class Ball{
    Vector2f m_position;
    CircleShape m_shape;
    float m_speed;
    float m_direction_x= 0.5f;
    float m_direction_y = 0.5f;
    int m_radius;
    Vector2f m_screenSize, m_initial_position;
public:
    Ball(int, Vector2f); //for Ball size only
    Ball(int, float, float, Vector2f); //for Ball size as wel as position
    FloatRect getPosition();
    CircleShape getShape();
    float getSpeed();
    void setSpeed(float);
    void reboundSides();
    void reboundTop();
    void reboundBottom();
    void reboundByBat();
    void update(Time);
    void resetPosition();
    float getXVelocity();
};