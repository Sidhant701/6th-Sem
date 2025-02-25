// 24/2/25

#include<SFML/Graphics.hpp>
#include<iostream>
using namespace sf;
using namespace std;

int main(){
    VideoMode vm(1920, 1080);
    RenderWindow window(vm, "Ga");
    Vector2u screenSize = window.getSize();
    cout<<screenSize.x<<" "<<screenSize.y<<endl;
    return 0;
}


// To Run in Terminal: g++ sfmlTest.cpp -o sfmlTest -lsfml-graphics -lsfml.window -lsfml-system
