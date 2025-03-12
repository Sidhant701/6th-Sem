#include <SFML/Graphics.hpp>
using namespace sf;

int main()
{
    VideoMode vm(1920, 1080);
    RenderWindow window(vm, "Timber Game!!", Style::Fullscreen);
    View view(FloatRect(0, 0, 1920, 1080));
    window.setView(view);

    bool paused=true,gameOver = true;

    Vector2u screenSize = window.getSize();
    // For background
    Texture textureBackground;
    textureBackground.loadFromFile("graphics/background.png");
    // Sprite spriteBackground;
    // spriteBackground.setTexture(textureBackground);
    Sprite spriteBackground(textureBackground);

    // For tree
    Texture textureTree;
    textureTree.loadFromFile("graphics/tree.png");
    Sprite spriteTree(textureTree);
    spriteTree.setPosition(810, 0);

    // For Bee
    Texture textureBee;
    textureBee.loadFromFile("graphics/bee.png");
    Sprite spriteBee(textureBee);
    spriteBee.setPosition(1800, 900);
    bool beeActive = false;
    float beeSpeed = 0.0f;

    // For Clouds
    Texture textureCloud;
    textureCloud.loadFromFile("graphics/cloud.png");
    // cloud1
    Sprite spriteCloud1(textureCloud), spriteCloud2(textureCloud), spriteCloud3(textureCloud);
    spriteCloud1.setPosition(0, 0);
    spriteCloud2.setPosition(0, 150);
    spriteCloud3.setPosition(0, 300);

    bool cloud1Active, cloud2Active, cloud3Active = false;
    float cloud1Speed, cloud2Speed, cloud3Speed = 0.0f;

    Font font;
    font.loadFromFile("fonts/KOMIKAP_.ttf");
    
    Text scoreText, pauseText, messageText;
    scoreText.setFont(font);
    pauseText.setFont(font);
    messageText.setFont(font);

    scoreText.setColor(Color::Red);
    pauseText.setColor(Color::White);
    messageText.setColor(Color::White);

    scoreText.setCharacterSize(100);
    pauseText.setCharacterSize(75);
    messageText.setCharacterSize(75);

    scoreText.setString("Score : 0");
    pauseText.setString("Press \'P\' to Puase/Unpause");
    messageText.setString("Press Enter to start");

    scoreText.setPosition(20,20);
    FloatRect rect =  pauseText.getLocalBounds();
    pauseText.setOrigin(rect.width/2.0,rect.height/2.0);
    pauseText.setPosition(view.getSize().x/2,view.getSize().y/2);

    messageText.setOrigin(messageText.getLocalBounds().width/2.0,messageText.getLocalBounds().height/2.0);
    messageText.setPosition(view.getSize().x/2,view.getSize().y/2);




    Clock clock;
    while (window.isOpen())
    {
        Time dt = clock.restart();
        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
            if(event.type == Event::KeyPressed && event.key.code == Keyboard::P && !gameOver){
                paused=!paused;
            }
        }

        if (Keyboard::isKeyPressed(Keyboard::Escape))
            window.close();

        // Start game
        if (Keyboard::isKeyPressed(Keyboard::Enter))
        {
            paused = false;
            gameOver = false;
        }

        if (!paused)
        {
            // Game area

            // For bee movement
            if (!beeActive)
            {
                // when bee is out of screen
                srand((int)time(0)*10);
                beeSpeed = (rand() % 200) + 200;

                srand((int)time(0)*20);
                float height = (rand() % 500) + 500;
                spriteBee.setPosition(2000, height);
                beeActive = true;
            }
            else
            {
                // when bee is in active mode
                float x = spriteBee.getPosition().x - dt.asSeconds() * beeSpeed;
                spriteBee.setPosition(x, spriteBee.getPosition().y);
                if (x < -100)
                    beeActive = false;
            }

            // For cloud1 movement
            if (!cloud1Active)
            {
                // when cloud1 is out of screen
                srand((int)time(0)*10);
                cloud1Speed = (rand() % 200) + 200;
                srand((int)time(0)*10);
                float height = (rand() % 150);
                spriteCloud1.setPosition(-100, height);
                srand((int)time(0)*10);
                float scale = ((rand()%60)+40)/100.0;
                spriteCloud1.setScale(scale,scale);
                cloud1Active = true;
            }
            else
            {
                // when cloud1 is in active mode
                float x = spriteCloud1.getPosition().x + dt.asSeconds() * cloud1Speed;
                spriteCloud1.setPosition(x, spriteCloud1.getPosition().y);
                if (x > 2000)
                    cloud1Active = false;
            }

            // For cloud2 movement
            if (!cloud2Active)
            {
                // when cloud1 is out of screen
                srand((int)time(0)*20);
                cloud2Speed = (rand() % 200) + 200;

                srand((int)time(0)*20);
                float height = (rand() % 300)-150;
                spriteCloud2.setPosition(-100, height);
                cloud2Active = true;
            }
            else
            {
                // when cloud1 is in active mode
                float x = spriteCloud2.getPosition().x + dt.asSeconds() * cloud2Speed;
                spriteCloud2.setPosition(x, spriteCloud2.getPosition().y);
                if (x > 2000)
                    cloud2Active = false;
            }

            // For cloud3 movement
            if (!cloud3Active)
            {
                // when cloud1 is out of screen
                srand((int)time(0)*20);
                cloud3Speed = (rand() % 200) + 200;

                srand((int)time(0)*20);
                float height = (rand() % 450)-300;
                spriteCloud3.setPosition(-100, height);
                cloud3Active = true;
            }
            else
            {
                // when cloud1 is in active mode
                float x = spriteCloud3.getPosition().x + dt.asSeconds() * cloud3Speed;
                spriteCloud3.setPosition(x, spriteCloud3.getPosition().y);
                if (x > 2000)
                    cloud3Active = false;
            }
        } // End of game play area

        // Draw the window
        window.clear();
        window.draw(spriteBackground);
        window.draw(spriteCloud1);
        window.draw(spriteCloud2);
        window.draw(spriteCloud3);
        window.draw(spriteTree);
        window.draw(spriteBee);

        window.draw(scoreText);
        if(gameOver)
            window.draw(messageText);
        if(paused && !gameOver)
            window.draw(pauseText);
        window.display();
    }
}