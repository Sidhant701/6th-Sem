#include "Ball.h"

Ball::Ball(int radius,Vector2f screenSize){
    m_screenSize = screenSize;
    m_radius = radius;
    m_Shape.setRadius(m_radius);
    m_Position = Vector2f(m_screenSize.x/2-m_radius,20);
    m_initial_position = m_Position;
    m_Shape.setPosition(m_Position);
}  // for size of bat
Ball::Ball(int radius,float posX,float posY,Vector2f screenSize){
    Ball(radius,screenSize);
    m_Position = Vector2f(posX,posY);
    m_initial_position = m_Position;
    m_Shape.setPosition(m_Position);
} // for size and position of bat
FloatRect Ball::getPosition(){
    return m_Shape.getGlobalBounds();
}
CircleShape& Ball::getShape(){
    return m_Shape;
}
void Ball::setSpeed(float speed){
    m_Speed = speed;
}
float Ball::getSpeed(){
    return m_Speed;
}
float Ball::getXVelocity(){
    return m_DirectionX;
}
void Ball::reboundSides(){
    m_DirectionX = -m_DirectionX;
}
void Ball::reboundTop(){
    m_DirectionY = -m_DirectionY;
}
void Ball::reboundBottom(){
    resetPosition();
}
void Ball::reboundByBat(){
    reboundTop();
}
void Ball::resetPosition(){
    m_Position = m_initial_position;
    m_Shape.setPosition(m_Position);
}

void Ball::update(Time dt){
    m_Position.x += m_Speed*dt.asSeconds()*m_DirectionX;
    m_Position.y += m_Speed*dt.asSeconds()*m_DirectionY;
    m_Shape.setPosition(m_Position);
}