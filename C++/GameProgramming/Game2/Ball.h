#pragma once
#include<SFML/Graphics.hpp>
using namespace sf;

class Ball{
private:
    Vector2f m_Position;
    Vector2f m_initial_position;
    CircleShape m_Shape;
    float m_Speed;
    int m_radius;  
    float m_DirectionX = 0.5f;
    float m_DirectionY = 0.5f;
    Vector2f m_screenSize;
public:
    Ball(int,Vector2f);  // for size of bat
    Ball(int,float,float,Vector2f); // for size and position of bat
    FloatRect getPosition();
    CircleShape& getShape();
    void setSpeed(float);
    float getSpeed();
    float getXVelocity();
    void reboundSides();
    void reboundTop();
    void reboundBottom();
    void reboundByBat();
    void resetPosition();
    void update(Time);
};