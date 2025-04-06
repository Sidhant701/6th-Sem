#include<SFML/Graphics.hpp>
using namespace sf;
// #ifndef BAT_SFML
// #define BAT_SFML
#pragma once
#include<SFML/Graphics.hpp>
// #endif
using namespace sf;

class Bat{
private:
    Vector2f m_Position;
    RectangleShape m_Shape;
    float m_Speed;
    int m_width;  // later we will do
    int m_height;  // later we will do
    bool m_MovingLeft = false;
    bool m_MovingRight = false;
    Vector2f m_screenSize;

public:
    Bat(int,int,Vector2f);  // for size of bat
    Bat(int,int,float,float,Vector2f); // for size and position of bat
    FloatRect getPosition();
    RectangleShape getShape();
    void setSpeed(float);
    float getSpeed();
    void setShape(RectangleShape);
    void moveLeft();
    void stopLeft();
    void moveRight();
    void stopRight();
    void update(Time);
};