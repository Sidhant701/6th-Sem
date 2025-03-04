// 3/3/25

// SFML: Simple & Fast Multimedia Library

// To Run in Terminal: g++ test.cpp -o test -lsfml-graphics -lsfml-window -lsfml-system
// Then type: ./test

#include <SFML/Graphics.hpp>
#include <iostream>
using namespace sf;
using namespace std;

int main()
{
	VideoMode vm(1366, 768); // enter resolution of Computer in brackets. Here, "1366 x 768".
	RenderWindow window(vm, "Test Window", Style::Fullscreen); // This line opens/renders the window.
	Vector2u screenSize = window.getSize();

	Color c(0,0,0);
	Color blue = Color::Blue;
	int radius = 150; // 150 is the radius in pixels.
	int r = 150;
	CircleShape circle1(radius);
	circle1.setFillColor(Color(255, 80, 0));
	CircleShape circle2(radius);
	circle2.setFillColor(Color(255, 80, 0));
	CircleShape circle3(radius);
	circle3.setFillColor(Color(255, 80, 0));
	CircleShape circle4(radius);
	circle4.setFillColor(Color(255, 80, 0));
	CircleShape circle5(r);
	circle5.setFillColor(Color(blue));

	cout<<"Circle Position x: "<<circle1.getPosition().x<<" y: "<<circle1.getPosition().y<<endl;

	// circle1's position is set to default
	// circle2.setPosition(1065,0); // (x,y) "MANUAL"
	circle2.setPosition(screenSize.x-2*radius, 0); // "Dynamic Right-Top"
	// circle3.setPosition(0,465);
	circle3.setPosition(0,screenSize.y-2*radius);
	// circle4.setPosition(1065,465);
	circle4.setPosition(screenSize.x-2*radius, screenSize.y-2*radius);
	// circle5.setPosition(screenSize.x-2*radius, 0); //right
	circle5.setPosition(screenSize.x/2-radius, screenSize.y/2-radius); //middle


	int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	// The below while loop is used to keep the window open, or else the window opens and closes within a second.
	while(window.isOpen()){
		// window.clear(Color::White); // Clears default styles. Adds new style (Color::<color>)
		// window.clear(Color(45, 87, 107)); // Clears default styles. Adds new style (Color(r,g,b))
		window.clear(Color(c));

		window.draw(circle1);
		window.draw(circle2);
		window.draw(circle3);
		window.draw(circle4);
		window.draw(circle5);

		// Animation
		circle1.setPosition(x1++,0);
		if(x1>screenSize.x)
			x1=0;
		circle2.setPosition(screenSize.x-2*radius,y1++);
		if(y1>screenSize.y)
			y1=0;
		circle3.setPosition(0,y2--);
		if(y2<0-2*radius)
			y2=screenSize.y-2*radius;
		circle4.setPosition(x2--,screenSize.y-2*radius);
		if(x2<0-2*radius)
			x2=screenSize.x-2*radius;

		circle5.setRadius(r--);
		circle5.setPosition(screenSize.x/2-r, screenSize.y/2-r);
		if(r<0){
			r = 150;
		}

		window.display();
	}
	return 0;
}
