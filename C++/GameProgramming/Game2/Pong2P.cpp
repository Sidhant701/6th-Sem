#include <SFML/Graphics.hpp>
#include "Bat.cpp"
#include "Ball.cpp"
using namespace sf;

int lives = 3;
const int MAXLIVES = 3;
int livingAppeaing[MAXLIVES];
Sprite liveSprite[MAXLIVES];


int main(){

    VideoMode vm(1920, 1080);
    RenderWindow window(vm, "Ping Pong Game", Style::Fullscreen);
    View view(FloatRect(0,0, 1920, 1080));
    window.setView(view);
    Vector2f screenSize = view.getSize();
    bool gameOver = false;

    int heart1_x_pos = 1708- 5;
    int heart2_x_pos = 1772- 5;
    int heart3_x_pos = 1836- 5;
    int heart_y = 30;

    Texture liveTexture;
    liveTexture.loadFromFile("heart.png");
    for(int i = 0;i< MAXLIVES;i++){
        liveSprite[i].setTexture(liveTexture);
        liveSprite[i].setScale(64.0f / 2000.0f,64.0f / 1214.0f);
    }
    liveSprite[0].setPosition(heart1_x_pos, heart_y);
    liveSprite[1].setPosition(heart2_x_pos, heart_y);
    liveSprite[2].setPosition(heart3_x_pos, heart_y);

    // Bat Object 
    int bat_height = 20, bat_width = 400;
    float bat_speed = 600;
    // Bat1
    Bat bat(bat_width, bat_height, screenSize);
    bat.setSpeed(bat_speed);
    bat.getShape().setFillColor(Color::White);
    // Bat2
    float posX = screenSize.x - bat_width/2;
    float posY = screenSize.y - bat_height - 1040;
    Bat bat2(bat_width, bat_height, posX, posY, screenSize);
    bat2.setSpeed(bat_speed);
    bat2.getShape().setFillColor(Color::White);

    // Ball
    int ball_radius = 15;
    float ball_speed = 650;
    Ball ball(ball_radius, screenSize);
    ball.setSpeed(ball_speed);
    ball.getShape().setFillColor(Color::Red);

    int score = 0;
    Font font;
    font.loadFromFile("DS-DIGI.TTF");

    // Score for bat 
    Text scoreText;
    scoreText.setFont(font);
    scoreText.setFillColor(Color::White);
    scoreText.setCharacterSize(75);
    scoreText.setPosition(20,20);
    scoreText.setString("Score1: 0");

    // Score for bat2 
    Text scoreText2;
    scoreText2.setFont(font);
    scoreText2.setFillColor(Color::White);
    scoreText2.setCharacterSize(75);
    scoreText2.setPosition(20,20+75);
    scoreText2.setString("Score2:0");

    Text messageText;
    messageText.setFont(font);
    messageText.setFillColor(Color::White);
    messageText.setCharacterSize(75);
    messageText.setPosition(20,20);
    messageText.setString("Game Over !!!,Press Enter to start again");
    messageText.setOrigin(messageText.getGlobalBounds().width/2, messageText.getGlobalBounds().height/2);
    messageText.setPosition(screenSize.x/2, screenSize.y/2);

    Text livesText;
    livesText.setFont(font);
    livesText.setFillColor(Color::White);
    livesText.setCharacterSize(75);
    livesText.setPosition(heart1_x_pos - 200, heart_y);
    livesText.setString("Lives: ");
    livesText.setFillColor(Color::White);



    Clock clock;
    while(window.isOpen()){
        Event event;
        while(window.pollEvent(event)){
            if(event.type == Event::Closed)
            window.close();
        }

        if(Keyboard::isKeyPressed(Keyboard::Escape)){
            window.close();
        }
        
        // bat movement
        if(Keyboard::isKeyPressed(Keyboard::Left)){
            bat.moveLeft();
        }
        else{
            bat.stopLeft();
        }
        if(Keyboard::isKeyPressed(Keyboard::Right)){
            bat.moveRight();
        }
        else{
            bat.stopRight();
        }
        
        // bat2 movement
        if(Keyboard::isKeyPressed(Keyboard::A)){
            bat2.moveLeft();
        }
        else{
            bat2.stopLeft();
        }
        if(Keyboard::isKeyPressed(Keyboard::D)){
            bat2.moveRight();
        }
        else{
            bat2.stopRight();
        }

        if(Keyboard::isKeyPressed(Keyboard::Enter) && gameOver){
            lives = 3;
            score = 0;
            gameOver = false;
            ball.resetPosition();
        }
        
        if(ball.getPosition().left <=0 || (ball.getPosition().left + 2* ball_radius) >= screenSize.x){
            ball.reboundSides();
        }
        
        if(ball.getPosition().top <= 0){
            // ball.reboundTop();
            lives--;
            // score++;
        } 

        if(ball.getPosition().top >= screenSize.y){
            ball.reboundBottom();
            lives--;
            if(lives == 0){
                gameOver = true;
            }
        }

        if(ball.getPosition().intersects(bat.getPosition())){
            ball.reboundByBat();
        }
        if(ball.getPosition().intersects(bat2.getPosition())){
            ball.reboundByBat();
        }

        scoreText.setString("Score1: "+std::to_string(score));
        scoreText2.setString("Score2:"+std::to_string(score));

        
        window.clear();
        Time dt = clock.restart();
        bat.update(dt);
        bat2.update(dt);
        
            
        ball.update(dt);
        if(!gameOver){
            window.draw(scoreText);
            window.draw(scoreText2);
            window.draw(livesText);
            for(int i=0;i <lives;i++){
                window.draw(liveSprite[i]);
            }
            window.draw(bat.getShape());
            window.draw(bat2.getShape());
            window.draw(ball.getShape());
            window.display();
        }
        else{
            window.draw(messageText);
            window.display();
        }

    }

    return 0;
}