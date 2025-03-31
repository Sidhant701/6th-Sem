#include"Bat.h"

Bat::Bat(int width, int height){
    m_width =  width;
    m_height = height;
    m_Shape = RectangleShape(Vector2f(m_width, m_height));
    m_Position = Vector2f((1920 - m_width) / 2 ,1080 - m_height);
} // for size of bat

Bat::Bat(int width, int height, float posX, float posY){
    Bat(width, height);
    m_Position = Vector2f(posX, posY);
    m_Shape.setPosition(m_Position);
}// for size and position of Bat


Vector2f Bat::getPosition(){
    return m_Position;
}

RectangleShape Bat::getShape(){
    return m_Shape;
}
void Bat::setShape(RectangleShape shape){
    m_Shape = shape;
    m_width = m_Shape.getLocalBounds().width;
    m_height = m_Shape.getLocalBounds().height;
    m_Shape.setPosition(m_Position);
}

void Bat::setSpeed(float speed){
    m_Speed = speed;
}
float Bat::getSpeed(){
    return m_Speed;
}

void Bat::moveLeft(){
    m_MovingLeft = true;
}
void Bat::stopLeft(){
    m_MovingLeft = false;
}
void Bat::moveRight(){
    m_MovingRight = true;
}
void Bat::stopRight(){
    m_MovingRight = false;
}

void Bat::update(Time dt, Vector2u screenSize){
    // Left
    if(m_MovingLeft){
        m_Position.x -= m_Speed * dt.asSeconds();
        if(m_Position.x < 0){
            m_Position.x = 0;
            m_MovingLeft = false;
        }
    }
    // Right
    if(m_MovingRight){
        m_Position.x += m_Speed * dt.asSeconds();
        if(m_Position.x >= (screenSize.x - m_width)){
            m_Position.x = 0;
            m_MovingRight = false;
        }
    }
    m_Shape = RectangleShape(Vector2f(m_width, m_height));
}


        