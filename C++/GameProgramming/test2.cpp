// 4/3/25

// To Run in Terminal: g++ test2.cpp -o test2 -lsfml-graphics -lsfml-window -lsfml-system
// Then type: ./test2

// Origin can be used to calculate distance between floating objects.

#include <SFML/Graphics.hpp>
#include <iostream>
using namespace sf;
using namespace std;

void drawGrid(RenderWindow &window, int spacing = 100){
    Color gridcolor(200,200,200,150);
    VertexArray lines(Lines);
    for (int i = 0; i < window.getSize().x; i+=spacing){
        lines.append(Vertex(Vector2f(i,0), gridcolor));
        lines.append(Vertex(Vector2f(i,window.getSize().y), gridcolor));
    }
    for (int i = 0; i < window.getSize().y; i+=spacing){
        lines.append(Vertex(Vector2f(0,i), gridcolor));
        lines.append(Vertex(Vector2f(window.getSize().x,i), gridcolor));
    }
    window.draw(lines);
}

int main(){
	VideoMode vm(1366, 768);
	RenderWindow window(vm, "Test Window", Style::Fullscreen);
	Vector2u screenSize = window.getSize();
    cout<<"Window Size x: "<<screenSize.x<<" y: "<<screenSize.y<<endl;

	Color c(45,30,34);
	Color blue = Color::Blue;
	int radius = 100;
	CircleShape circle1(radius), circle2(radius);
	circle1.setFillColor(Color::Magenta);
	circle2.setFillColor(Color(blue));

    circle1.setPosition(0+radius,0+radius);
    circle2.setPosition(screenSize.x-2*radius,0); // Right-Top

    cout<<"Position: ("<<circle1.getPosition().x<<","<<circle1.getPosition().y<<")"<<endl;
    cout<<"Origin: ("<<circle1.getOrigin().x<<","<<circle1.getOrigin().y<<")"<<endl;
    
    FloatRect localrect = circle1.getLocalBounds();
    FloatRect globalrect = circle1.getGlobalBounds();
    cout<<"LocalBound: "<<localrect.left<<","<<localrect.top<<" "<<localrect.width<<","<<localrect.height<<endl;
    cout<<"GlobalBound: "<<globalrect.left<<","<<globalrect.top<<" "<<globalrect.width<<","<<globalrect.height<<endl;


    cout<<"\nAfter Chaning Origin:-"<<endl;
    circle1.setOrigin(50,50);
    cout<<"Position: ("<<circle1.getPosition().x<<","<<circle1.getPosition().y<<")"<<endl;
    cout<<"Origin: ("<<circle1.getOrigin().x<<","<<circle1.getOrigin().y<<")"<<endl;
    localrect = circle1.getLocalBounds();
    globalrect = circle1.getGlobalBounds();
    cout<<"LocalBound: "<<localrect.left<<","<<localrect.top<<" "<<localrect.width<<","<<localrect.height<<endl;
    cout<<"GlobalBound: "<<globalrect.left<<","<<globalrect.top<<" "<<globalrect.width<<","<<globalrect.height<<endl;



    int x = 0;
    while(window.isOpen()){
        Event event;
        while(window.pollEvent(event)){
            if(event.type == Event::Closed){
                window.close();
            }
        }
        window.clear(c);
        drawGrid(window, 100);
        window.draw(circle1);
        window.draw(circle2);
        window.display();
    }
    return 0;
}

// Texture Class: For loading Object
// sprite Class: For movable object and texture