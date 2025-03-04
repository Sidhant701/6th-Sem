// 25/2/25

#include<iostream>
using namespace std;

class B;
class A{
    int var1;
    public:
        A(){var1 = 0;}
        A(int a){
            var1 = a;
        }
    friend int max(A,B); //Need to define it
    void display(){
        cout<<"A: "<<var1<<endl;
    }
};
class B{
    int var1;
    public:
        B(){var1 = 0;}
        B(int a){
            var1 = a;
        }
    friend int max(A,B);
    void display(){
        cout<<"B: "<<var1<<endl;
    }
};

int main(){
    A a(10);
    B b(20);
    a.display();
    b.display();
    // cout<<"Max: "<<max(a,b)<<endl;
    return 0;
}
