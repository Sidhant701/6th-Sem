#include<SFML/Graphics.hpp>
using namespace sf;

class Bat{
    private:
        Vector2f m_Position;
        RectangleShape m_Shape;
        float m_Speed;
        int m_width; // later
        int m_height; // later
        bool m_MovingLeft = false;
        bool m_MovingRight = false;


    public:
        Bat(int, int); // for size of Bat
        Bat(int, int, float, float); // for size and position of Bat


        Vector2f getPosition();

        RectangleShape getShape();
        void setShape(RectangleShape);

        void setSpeed(float);
        float getSpeed();

        void moveLeft();
        void stopLeft();
        void moveRight();
        void stopRight();

        void update(Time, Vector2u);

};

