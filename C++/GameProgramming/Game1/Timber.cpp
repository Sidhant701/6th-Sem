#include<SFML/Graphics.hpp>
using namespace sf;

int main(){
    // int resX = 1366, resY = 768;
    int resX = 1920 , resY = 1080;
    VideoMode vm(resX, resY);
    RenderWindow window(vm, "Timber Game!!", Style::Fullscreen);
    View view(FloatRect(0,0,resX,resY));
    window.setView(view);

    bool paused = true, gameOver = true;

    Vector2u screenSize = window.getSize();
    
    // Background
    Texture textureBackground;
    textureBackground.loadFromFile("graphics/background.png");
    Sprite spriteBackground(textureBackground);
    // spriteBackground.setTexture(textureBackground);
    // spriteBackground.setPosition(0,0);
    // spriteBackground.setScale(1,1);
    // spriteBackground.setOrigin(0,0);

    // Tree
    Texture textureTree;
    textureTree.loadFromFile("graphics/tree.png");
    Sprite spriteTree(textureTree);
    spriteTree.setPosition(resX/2-100,0);
    spriteTree.setOrigin(0,0);

    // Bee
    Texture textureBee;
    textureBee.loadFromFile("graphics/bee.png");
    Sprite spriteBee(textureBee);
    spriteBee.setPosition(resX/2-100,resY/2);
    bool beeActive = false;
    float beeSpeed = 0.2f;


    // CLOUDS
    Texture textureCloud;
    textureCloud.loadFromFile("graphics/cloud.png");
    Sprite spriteCloud1(textureCloud), spriteCloud2(textureCloud), spriteCloud3(textureCloud);
    bool cloud1Active, cloud2Active, cloud3Active = false;    
    
    // cloud1
    spriteCloud1.setPosition(0,0);
    float c1Speed = 0.1f;
    // cloud2
    spriteCloud2.setPosition(0,150);
    float c2Speed = 0.05f;
    // cloud3
    spriteCloud3.setPosition(0,300);
    spriteCloud3.setScale(0.6f,0.6f);
    float c3Speed = 0.15f;

    // FONTS
    Font font;
    font.loadFromFile("fonts/KOMIKAP_.ttf");

    Text scoreText, pauseText, messageText, gameOverText;
    scoreText.setFont(font);
    pauseText.setFont(font);
    messageText.setFont(font);
    gameOverText.setFont(font);

    scoreText.setColor(Color::Red);
    pauseText.setColor(Color::White);
    messageText.setColor(Color::White);
    gameOverText.setColor(Color::White);

    scoreText.setCharacterSize(100);
    scoreText.setCharacterSize(75);
    scoreText.setCharacterSize(75);
    gameOverText.setCharacterSize(75);
    
    scoreText.setString("Score: 0");
    pauseText.setString("Press \'P\' to Pause/Unpause");
    messageText.setString("Press \'Enter\' to Start");
    gameOverText.setString("");

    scoreText.setPosition(20,20);
    FloatRect rect = pauseText.getLocalBounds();
    pauseText.setOrigin(rect.width/2.0,rect.height/2.0);
    pauseText.setPosition(view.getSize().x/2, view.getSize().y/2);
    pauseText.setScale(2,2);
    
    messageText.setOrigin(messageText.getLocalBounds().width / 2.0, messageText.getLocalBounds().height / 2.0);
    messageText.setPosition(view.getSize().x / 2, view.getSize().y / 2);
    messageText.setScale(2,2);
    
    // TIMEBAR
    const float maxWidthTimeBar = 400.0f;
    const float maxHeightTimeBar = 75.0f;

    RectangleShape timeBar(Vector2f(maxWidthTimeBar, maxHeightTimeBar));
    timeBar.setFillColor(Color::Red);
    timeBar.setPosition((view.getSize().x - maxWidthTimeBar) / 2, view.getSize().y - 100);

    float timeRemaining = 6.0f;
    const float widthPerTime = maxWidthTimeBar / timeRemaining;


    Clock clock;

    int x = 0;
    while(window.isOpen()){
        Time dt = clock.restart();
        Event event;
        while(window.pollEvent(event)){
            if (event.type == Event::Closed)
                window.close();
            if (event.type == Event::KeyPressed && event.key.code == Keyboard::P && !gameOver){
                paused = !paused;
            }
        }

        // * pollEvent: Discrete Event
        // * isKeyPressed: Continuous Event
        
        // Esc to Quit
		if(Keyboard::isKeyPressed(Keyboard::Escape)){
			window.close();
		}
        // Enter to Start
		if(Keyboard::isKeyPressed(Keyboard::Enter) && gameOver){
            timeRemaining = 6.0f;
            paused = false;
            gameOver = false;
		}
        // P to Pause/Unpause
		if(Keyboard::isKeyPressed(Keyboard::P)){
			paused = !paused;
            while(Keyboard::isKeyPressed(Keyboard::P)){
                // Do nothing, wait for key release
            }
		}
        
        if(!paused){
            // Game Area
            
            // TimeBar Movement
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
            }

            if(!beeActive){
                srand((int)time(0) * 10);
                beeSpeed = (rand()%200)+200;

                srand((int)time(0)*20);
                float height = (rand()%500)+500;
                spriteBee.setPosition(2000, height);
                beeActive = true;
            }
            else{
                // When bee is in active mode
                float x =  spriteBee.getPosition().x - dt.asSeconds()*1000;
                spriteBee.setPosition(x, spriteBee.getPosition().y);
                if(x<-100){
                    beeActive = false;
                }
            }

            // Clouds Animations
            if(!cloud1Active){ 
                float scale = ((rand()%60)+40)/100.0f;
                spriteCloud1.setScale(scale,scale);
                float height = (rand()%200);
                spriteCloud1.setPosition(0, height);
                cloud1Active = true;
            }
            else{
                float x1 = spriteCloud1.getPosition().x + dt.asSeconds()*1000*c1Speed;
                spriteCloud1.setPosition(x1, spriteCloud1.getPosition().y) ;
                if(x1>2000) cloud1Active = false;
            }
            if(!cloud2Active){
                float scale = ((rand()%60)+40)/100.0f;
                spriteCloud1.setScale(scale,scale);
                float height = (rand()%200);
                spriteCloud2.setPosition(0, height);
                cloud2Active = true;
            }
            else{
                float x2 = spriteCloud2.getPosition().x + dt.asSeconds()*1000*c2Speed;
                spriteCloud2.setPosition(x2, spriteCloud2.getPosition().y) ;
                if(x2>2000) cloud2Active = false;
            }
            if(!cloud3Active){
                float scale = ((rand()%60)+40)/100.0f;
                spriteCloud1.setScale(scale,scale);
                float height = (rand()%200);
                spriteCloud3.setPosition(0, height);
                cloud3Active = true;
            }
            else{
                float x3 = spriteCloud3.getPosition().x + dt.asSeconds()*1000*c3Speed;
                spriteCloud3.setPosition(x3, spriteCloud3.getPosition().y) ;
                if(x3>2000) cloud3Active = false;
            }
        }
        
        window.clear();
        window.draw(spriteBackground);
        window.draw(spriteCloud1);
        window.draw(spriteCloud2);
        window.draw(spriteCloud3);
        window.draw(spriteTree);
        window.draw(spriteBee);

        window.draw(scoreText);
        window.draw(scoreText);
        if (gameOver)
        {
            window.draw(messageText);
            window.draw(gameOverText);
        }
        if (paused && !gameOver)
            window.draw(pauseText);
        window.draw(timeBar);

        window.display();
    }
    return 0;
}