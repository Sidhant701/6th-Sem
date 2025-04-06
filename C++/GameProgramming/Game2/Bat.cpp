#include"Bat.h"

Bat::Bat(int width,int height,Vector2f screenSize){
    m_screenSize = screenSize;
    m_width = width;
    m_height = height;
    m_Shape = RectangleShape(Vector2f(m_width,m_height));
    m_Position = Vector2f((m_screenSize.x-m_width)/2,m_screenSize.y-m_height-20);
    m_Shape.setPosition(m_Position);
}  // for size of bat

Bat::Bat(int width,int height,float posX,float posY,Vector2f screenSize){
    Bat(width,height,screenSize);
    m_Position = Vector2f(posX,posY);
    m_Shape.setPosition(m_Position);
} // for size and position of bat

FloatRect Bat::getPosition(){
    return m_Shape.getGlobalBounds();
}
RectangleShape Bat::getShape(){
    return m_Shape;
}
void Bat::setSpeed(float speed){
    m_Speed = speed;
}
float Bat::getSpeed(){
    return m_Speed;
}
void Bat::setShape(RectangleShape shape){
    m_Shape = shape;
    m_width = m_Shape.getLocalBounds().width;
    m_height = m_Shape.getLocalBounds().height;
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
void Bat::update(Time dt){
    if(m_MovingLeft){
        m_Position.x -= (m_Speed*dt.asSeconds());
        if(m_Position.x <= 0){
            m_Position.x = 0;
            m_MovingLeft = false;
        } 
    }
    if(m_MovingRight){
        m_Position.x += (m_Speed*dt.asSeconds());
        if(m_Position.x >= (m_screenSize.x-m_width)){
            m_Position.x = m_screenSize.x-m_width;
            m_MovingRight = false;
        } 
    }
    m_Shape.setPosition(m_Position);
}