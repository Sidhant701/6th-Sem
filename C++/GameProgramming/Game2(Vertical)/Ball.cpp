#include "Ball.h"


Ball::Ball(int radius, Vector2f screenSize){
    m_radius = radius;
    m_shape.setRadius(radius);
    m_screenSize = screenSize;
    m_position = Vector2f((m_screenSize.x/2-m_radius), 20);
    m_initial_position = m_position;
    m_shape.setPosition(m_position);
} //for Ball size only
Ball::Ball(int radius,  float pos_x, float pos_y, Vector2f screenSize){
    Ball(radius, screenSize);
    m_position = Vector2f(pos_x, pos_y);
    m_initial_position = m_position;
    m_shape.setPosition(m_position);
} //for Ball size as wel as position
FloatRect Ball::getPosition(){
    return m_shape.getGlobalBounds();
}
CircleShape Ball::getShape(){
    return m_shape;
}
float Ball::getSpeed(){
    return m_speed;
}
void Ball::setSpeed(float speed){
    m_speed = speed;
}
float Ball::getXVelocity(){
    return m_direction_x;
}
void Ball::reboundSides(){
    m_direction_x = -m_direction_x;
}
void Ball::reboundTop(){
    m_direction_y = -m_direction_y;
}
void Ball::reboundBottom(){
    resetPosition();
}
void Ball::resetPosition(){
    m_position = m_initial_position;
    m_shape.setPosition(m_position);
}
void Ball::reboundByBat(){
    reboundTop();
}
void Ball::update(Time dt){
    m_position.x += m_direction_x * m_speed * dt.asSeconds();
    m_position.y += m_direction_y * m_speed * dt.asSeconds();
    m_shape.setPosition(m_position);
}