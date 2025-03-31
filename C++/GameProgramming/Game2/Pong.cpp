#include<SFML/Graphics.hpp>
#include"Bat.cpp"

int main(){
    // VideoMode vm(1920, 1080);
    VideoMode vm(1600, 900);
    RenderWindow window(vm, "Pong Game", Style::Fullscreen);
    View view(FloatRect(0, 0, 1920, 1080));
    window.setView(view);
    Vector2f screenSize = view.getSize();

    int bat_height = 50;
    int bat_width = 300;
    float bat_speed = 600;

    Bat bat(bat_width, bat_height);
    bat.setSpeed(bat_speed);
    bat.getShape().setFillColor(Color::White);

    while (window.isOpen()){
        Event event;
        while (window.pollEvent(event)){
            if (event.type == Event::Closed)
                window.close();
        }
        if(Keyboard::isKeyPressed(Keyboard::Escape)){
            window.close();
        }

        
        // window update
        // draw window
        window.clear();
        window.draw(bat.getShape());
        
        window.display();


    }
    

    return 0;
}
