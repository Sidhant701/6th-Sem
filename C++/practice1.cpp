// Constructor

// #include<iostream>
// using namespace std;

// class Integer{
//     int m,n;
//     public:
//         Integer(int m, int n){
//             this->m = m;
//             this->n = n;
//             cout<<"Integer Initialized as: "<<m<<"."<<n<<endl;

//         } 
//     public:
//         Integer(){};
//     void init(int m, int n){
//         this->m = m;
//         this->n = n;
//         cout<<"Integer Initialized as: "<<m<<"."<<n<<endl;
//     }
// };

// int main(){
//     Integer i1(10,5);
//     // Integer i1(11,5); // Causes error (because of redeclaration)
//     Integer i2;
//     i2.init(2,5);
//     i2.init(4,5);
//     i2.init(3,5);
//     return 0;
// }


// 25/2/25
// Without COPY Constructor
#include<iostream>
using namespace std;

class Test{
    public: int a,b;
    public:
        Test(){}
        Test(int a, int b){
            this->a = a;
            this->b = b;
        }
    void display(){
        cout<<"a = "<<a<<", b = "<<b<<endl;
    }
};
int main(){
    Test t1(10,20);
    t1.display();
    Test t2;
    t1.a = 5;
    t1.display();
    t2 = t1;
    t2.display();
    return 0;
}
// t2 is a shallow copy.