#include "Bat.h"

    Bat::Bat(int width, int height, Vector2f screenSize){
        m_width = width;
        m_height = height;
        m_shape = RectangleShape(Vector2f(m_width, m_height));
        m_screenSize = screenSize;
        m_position = Vector2f((m_screenSize.x-m_width)/2, (m_screenSize.y-m_height) - 20);
        m_shape.setPosition(m_position);
    } 
    Bat::Bat(int width, int height, float pos_x, float pos_y, Vector2f screenSize){
        m_width = width;
        m_height = height;
        m_shape = RectangleShape(Vector2f(m_width, m_height));
        m_screenSize = screenSize;
        m_position = Vector2f(pos_x, pos_y);
        m_shape.setPosition(m_position);
    } 
    FloatRect Bat::getPosition(){
        return m_shape.getGlobalBounds();
    }
    RectangleShape Bat::getShape(){
        return m_shape;
    }
    float Bat::getSpeed(){
        return m_speed;
    }
    void Bat::setSpeed(float speed){
        m_speed = speed;
    }
    void Bat::setShape(RectangleShape shape){
        m_shape = shape;
        m_width = m_shape.getLocalBounds().width;
        m_height = m_shape.getLocalBounds().height;
    }
    void Bat::moveLeft(){
        m_moving_left = true;
    }
    void Bat::stopLeft(){
        m_moving_left = false;
    }
    void Bat::moveRight(){
        m_moving_right = true;
    }
    void Bat::stopRight(){
        m_moving_right = false;
    }
    void Bat::update(Time dt){
        if(m_moving_left){
            m_position.x -= m_speed * dt.asSeconds();
        }
        if(m_moving_right){
            m_position.x += m_speed * dt.asSeconds();
        }
        if(m_position.x < 0){
            m_position.x = 0;
            stopLeft();
        }
        if(m_position.x > m_screenSize.x - m_width){
            m_position.x = m_screenSize.x - m_width;
            stopRight();
        }
        m_shape.setPosition(m_position);
    }