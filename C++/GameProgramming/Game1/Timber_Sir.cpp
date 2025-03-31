#include <SFML/Graphics.hpp>
#include<SFML/Audio.hpp>
#include <iostream>
using namespace sf;

enum class Side
{
    LEFT,
    RIGHT,
    NONE
};
const int NUM_BRANCHES = 6;
Sprite spriteBranches[NUM_BRANCHES];
Side brachPositions[NUM_BRANCHES];

void updateBranchPosition(int);
int main()
{
    VideoMode vm(1920, 1080);
    RenderWindow window(vm, "Timber Game!!", Style::Fullscreen);
    View view(FloatRect(0, 0, 1920, 1080));
    window.setView(view);

    const int player_L = 510;
    const int player_R = 1260;
    const int axe_L = 660;
    const int axe_R = 1110;

    Side playerPosition = Side::LEFT;

    bool paused = true, gameOver = true;

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

    Text scoreText, pauseText, messageText, gameOverText;
    scoreText.setFont(font);
    pauseText.setFont(font);
    messageText.setFont(font);
    gameOverText.setFont(font);

    scoreText.setFillColor(Color::Red);
    pauseText.setFillColor(Color::White);
    messageText.setFillColor(Color::White);
    gameOverText.setFillColor(Color::White);

    scoreText.setCharacterSize(100);
    pauseText.setCharacterSize(75);
    messageText.setCharacterSize(75);
    gameOverText.setCharacterSize(75);

    scoreText.setString("Score : 0");
    pauseText.setString("Press \'P\' to Puase/Unpause");
    messageText.setString("Press Enter to start");
    gameOverText.setString("");

    scoreText.setPosition(20, 20);
    FloatRect rect = pauseText.getLocalBounds();
    pauseText.setOrigin(rect.width / 2.0, rect.height / 2.0);
    pauseText.setPosition(view.getSize().x / 2, view.getSize().y / 2);

    messageText.setOrigin(messageText.getLocalBounds().width / 2.0, messageText.getLocalBounds().height / 2.0);
    messageText.setPosition(view.getSize().x / 2, view.getSize().y / 2);

    const float maxWidthTimeBar = 400.0f;
    const float maxHeightTimeBar = 75.0f;

    RectangleShape timeBar(Vector2f(maxWidthTimeBar, maxHeightTimeBar));
    timeBar.setFillColor(Color::Red);
    timeBar.setPosition((view.getSize().x - maxWidthTimeBar) / 2, view.getSize().y - 100);

    float timeRemaining = 6.0f;
    const float widthPerTime = maxWidthTimeBar / timeRemaining;

    Texture texturePlayer;
    texturePlayer.loadFromFile("graphics/player.png");
    Sprite spritePlayer(texturePlayer);
    spritePlayer.setPosition(player_L, 750);

    Texture textureAxe;
    textureAxe.loadFromFile("graphics/axe.png");
    Sprite spriteAxe(textureAxe);
    spriteAxe.setPosition(axe_L, 850);

    Texture textureRIP;
    textureRIP.loadFromFile("graphics/rip.png");
    Sprite spriteRIP(textureRIP);
    spriteRIP.setPosition(player_L, 790);

    Texture textureLog;
    textureLog.loadFromFile("graphics/log.png");
    Sprite spriteLog(textureLog);
    spriteLog.setPosition(3000, 3000);

    bool logActive = false;
    float logXSpeed = 5000;
    float logYSpeed = 1500;

    Texture textureBranch;
    textureBranch.loadFromFile("graphics/branch.png");
    for (int i = 0; i < NUM_BRANCHES; i++)
    {
        spriteBranches[i].setTexture(textureBranch);
        spriteBranches[i].setOrigin(220, 40);
        spriteBranches[i].setPosition(2000,2000);
    }
    for (int i = 0; i < NUM_BRANCHES-1; i++)
    {
        updateBranchPosition(i);
    }

    bool actionInput = false;
    int score = 0;

    SoundBuffer chopBuffer;
    chopBuffer.loadFromFile("audio/chop.wav");
    Sound chop(chopBuffer);

    SoundBuffer deathBuffer;
    deathBuffer.loadFromFile("audio/death.wav");
    Sound death(deathBuffer);

    SoundBuffer ootBuffer;
    ootBuffer.loadFromFile("audio/out_of_time.wav");
    Sound oot(ootBuffer);

    Clock clock;
    while (window.isOpen())
    {
        Time dt = clock.restart();
        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
            if (event.type == Event::KeyPressed && event.key.code == Keyboard::P && !gameOver)
            {
                paused = !paused;
            }
            if (event.type == Event::KeyPressed && event.key.code == Keyboard::Left && !paused && !logActive)
            {
                playerPosition = Side::LEFT;
                score++;
                timeRemaining += (2.0f / score) + 0.15f;
                if (timeRemaining > 6.0f)
                    timeRemaining = 6.0f;
                spritePlayer.setPosition(player_L, spritePlayer.getPosition().y);
                spriteAxe.setPosition(axe_L, spriteAxe.getPosition().y);
                spriteLog.setPosition(810, 780);
                logActive = true;
                logXSpeed = -6000;
                updateBranchPosition(score);
                chop.play();
            }
            if (event.type == Event::KeyPressed && event.key.code == Keyboard::Right && !paused && !logActive)
            {
                playerPosition = Side::RIGHT;
                score++;
                timeRemaining += (2.0f / score) + 0.15f;
                if (timeRemaining > 6.0f)
                    timeRemaining = 6.0f;
                spritePlayer.setPosition(player_R, spritePlayer.getPosition().y);
                spriteAxe.setPosition(axe_R, spriteAxe.getPosition().y);
                spriteLog.setPosition(810, 780);
                logActive = true;
                logXSpeed = 6000;
                updateBranchPosition(score);
                chop.play();
            }
            if (event.type == Event::KeyReleased && (event.key.code == Keyboard::Left || event.key.code == Keyboard::Right) && !paused)
            {
                spriteAxe.setPosition(3000, spriteAxe.getPosition().y);
            }
        }

        if (Keyboard::isKeyPressed(Keyboard::Escape))
            window.close();

        // Start game
        if (Keyboard::isKeyPressed(Keyboard::Enter) && gameOver)
        {
            timeRemaining = 6.0f;
            score = 0;
            paused = false;
            gameOver = false;
            spriteRIP.setPosition(3000, spriteRIP.getPosition().y);
            brachPositions[4] = Side::NONE;
            brachPositions[5] = Side::NONE;
        }

        if (!paused)
        {

            // Game area
            timeRemaining -= dt.asSeconds();
            timeBar.setSize(Vector2f(widthPerTime * timeRemaining, maxHeightTimeBar));
            if (timeRemaining <= 0)
            {
                gameOver = true;
                paused = true;
                gameOverText.setString("Out of Time");
                FloatRect rect = gameOverText.getLocalBounds();
                gameOverText.setOrigin(rect.width / 2.0, rect.height / 2.0);
                gameOverText.setPosition(view.getSize().x / 2, view.getSize().y / 2 - 100);
                oot.play();
            }
            // For bee movement
            if (!beeActive)
            {
                // when bee is out of screen
                srand((int)time(0) * 10);
                beeSpeed = (rand() % 200) + 200;

                srand((int)time(0) * 20);
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
                srand((int)time(0) * 10);
                cloud1Speed = (rand() % 200) + 200;
                srand((int)time(0) * 10);
                float height = (rand() % 150);
                spriteCloud1.setPosition(-100, height);
                srand((int)time(0) * 10);
                float scale = ((rand() % 60) + 40) / 100.0;
                spriteCloud1.setScale(scale, scale);
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
                srand((int)time(0) * 20);
                cloud2Speed = (rand() % 200) + 200;

                srand((int)time(0) * 20);
                float height = (rand() % 300) - 150;
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
                srand((int)time(0) * 20);
                cloud3Speed = (rand() % 200) + 200;

                srand((int)time(0) * 20);
                float height = (rand() % 450) - 300;
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

            // Placement of Branches
            for (int i = 0; i < NUM_BRANCHES; i++)
            {
                int y_pos = i * 150;
                // std::cout<<(int)brachPositions[i]<<std::endl;
                if (brachPositions[i] == Side::LEFT)
                {
                    // std::cout<<"AAA\n";
                    spriteBranches[i].setPosition(600, y_pos);
                    spriteBranches[i].setRotation(180);
                }
                if (brachPositions[i] == Side::RIGHT)
                {
                    spriteBranches[i].setPosition(1260, y_pos);
                    spriteBranches[i].setRotation(0);
                }
                if (brachPositions[i] == Side::NONE)
                {
                    spriteBranches[i].setPosition(3000, y_pos);
                }
            }
            if (playerPosition == brachPositions[5])
            {
                gameOver = true;
                paused = true;
                if (playerPosition == Side::LEFT)
                    spriteRIP.setPosition(player_L, spriteRIP.getPosition().y);
                if (playerPosition == Side::RIGHT)
                    spriteRIP.setPosition(player_R, spriteRIP.getPosition().y);
                gameOverText.setString("Squished...");
                FloatRect rect = gameOverText.getLocalBounds();
                gameOverText.setOrigin(rect.width / 2.0, rect.height / 2.0);
                gameOverText.setPosition(view.getSize().x / 2, view.getSize().y / 2 - 100);
                death.play();
            }
            scoreText.setString("Score: " + std::to_string(score));
            if (logActive)
            {
                float newX = spriteLog.getPosition().x + logXSpeed * dt.asSeconds();
                float newY = spriteLog.getPosition().y - logYSpeed * dt.asSeconds();
                spriteLog.setPosition(newX, newY);
                if ((newX < -300 || newX > 2200) || newY < -100)
                {
                    logActive = false;
                }
            }
        } // End of game play area

        // Draw the window
        window.clear();
        window.draw(spriteBackground);
        window.draw(spriteCloud1);
        window.draw(spriteCloud2);
        window.draw(spriteCloud3);
        window.draw(spriteTree);
        for (int i = 0; i < NUM_BRANCHES; i++)
        {
            window.draw(spriteBranches[i]);
        }
        window.draw(spriteBee);

        window.draw(scoreText);
        if (gameOver)
        {
            window.draw(messageText);
            window.draw(gameOverText);
        }
        if (paused && !gameOver)
            window.draw(pauseText);
        window.draw(timeBar);
        window.draw(spritePlayer);
        window.draw(spriteAxe);

        window.draw(spriteRIP);
        window.draw(spriteLog);
        window.display();
    }
}

void updateBranchPosition(int seed)
{
    for (int i = NUM_BRANCHES - 1; i >= 1; i--)
    {
        brachPositions[i] = brachPositions[i - 1];
    }
    srand((int)(time(0))*seed);
    int pos = rand() % 4;
    switch (pos)
    {
    case 0:
        brachPositions[0] = Side::LEFT;
        break;
    case 1:
        brachPositions[0] = Side::RIGHT;
        break;
    default:
        brachPositions[0] = Side::NONE;
        break;
    }
}