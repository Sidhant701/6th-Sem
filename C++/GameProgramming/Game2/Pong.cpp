#include <SFML/Graphics.hpp>
#include "Bat.cpp"
#include "Ball.cpp"
using namespace sf;

int main(){
    // VideoMode vm(1920, 1080);
    VideoMode vm(1600, 900);
    RenderWindow window(vm, "Pong Game", Style::Fullscreen);
    View view(FloatRect(0, 0, 1920, 1080));
    window.setView(view);
    Vector2f screenSize = view.getSize();

    // int bat_height = 10;
    int bat_height = 50;
    int bat_width = 300;
    float bat_speed = 600;

    Bat bat(bat_width, bat_height, screenSize);
    bat.setSpeed(bat_speed);
    bat.getShape().setFillColor(Color::White);

    int ball_radius = 15;
    float ball_speed = 1000;
    Ball ball(ball_radius, screenSize);
    ball.setSpeed(ball_speed);
    ball.getShape().setFillColor(Color::Red);
    Clock clock;

    Font font;
    font.loadFromFile("fonts/DS-DIGI.TTF");

    int score = 0;
    Text scoreText;
    scoreText.setFont(font);
    scoreText.setFillColor(Color::White);
    scoreText.setCharacterSize(75);
    scoreText.setPosition(20,20);
    scoreText.setString("Score: 0");

    bool gameOver = false;


    while (window.isOpen()){
        Event event;
        while (window.pollEvent(event)){
            if (event.type == Event::Closed)
                window.close();
        }
        if(Keyboard::isKeyPressed(Keyboard::Escape)){
            window.close();
        }


        // Movement of Bat
        if (Keyboard::isKeyPressed(Keyboard::Left))
            bat.moveLeft();
        else
            bat.stopLeft();
        if (Keyboard::isKeyPressed(Keyboard::Right))
            bat.moveRight();
        else
            bat.stopRight();

        // update window
        Time dt = clock.restart();
        bat.update(dt);
        ball.update(dt);

        if (ball.getPosition().left <= 0 || (ball.getPosition().left + 2 * ball_radius) >= screenSize.x)
            ball.reboundSides();
        if (ball.getPosition().top <= 0){
            ball.reboundTop();
            score++;
        }
        if (ball.getPosition().top >= screenSize.y){
            gameOver = true;
            ball.reboundBottom();
            ///
        }
        if(ball.getPosition().intersects(bat.getPosition())){
            ball.reboundByBat();
        }

        scoreText.setString("Score: "+ std::to_string(score));

            // draw window
        window.clear();
        window.draw(bat.getShape());
        window.draw(ball.getShape());
        window.draw(scoreText);
        window.display();
    }

    return 0;
}
