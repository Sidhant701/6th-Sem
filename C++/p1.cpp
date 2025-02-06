// 27/01/2025

// #include <iostream>
// using namespace std;

// int main() {
//     // // WITHOUT using namespace std;
//     // int i;
//     // std::cout << "Enter Value: ";
//     // std::cin >> i;
//     // std::cout << "Hello World in CPP\n";
//     // std::cout << "Value of i is "<<i<<": Thank You!!!\n";
//     // return 0;

//     // WITH using namespace std;
//     int i;
//     cout << "Enter Value: ";
//     cin >> i;
//     cout << "Hello World in CPP\n";
//     cout << "Value of i is " << i << ": Thank You!!!\n";
//     return 0;
// }


// 28/01/25
#include <iostream>
using namespace std;

void swap_v(int a, int b){
    int temp = a;
    a = b;
    b = temp;
}
void swap_a(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void swap_r(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int a = 10, b = 5;
    cout << "Before swapping: a = " << a << ", b = " << b << endl;
    // swap_v(a, b); // Doesn't Work
    // cout << "After swapping: a = " << a << ", b = " << b << endl;
    // swap_a(&a, &b); // Works
    // cout << "After swapping: a = " << a << ", b = " << b << endl;
    swap_r(a, b); // Works
    cout << "After swapping: a = " << a << ", b = " << b << endl;
    return 0;
}
