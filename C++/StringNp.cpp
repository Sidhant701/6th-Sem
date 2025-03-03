// 25/2/25

#include<iostream>
#include<string.h>
using namespace std;

class String{
    // private:
    public:
        char *data;
        int len;
        String(){
            data = NULL;
        }
    String(char *str){
        len = strlen(str);
        data = new char[len+1];
        strcpy(data, str);
    }
    void myUpper(){
        for (int i = 0; i < len; i++){
            data[i] += 32; 
        }
    }
    String join(String b){
        String temp;
        temp.len = this->len+b.len;
        temp.data = new char[temp.len+1];
        strcpy(temp.data, this->data);
        strcat(temp.data, b.data);
        return temp;
    }
    void display(){
        cout<<data<<endl;
    }
};

int main(){
    String s1("Hello");
    s1.display();
    String s2 = "World!";
    s2.display();
    
    String s3 = s1.join(s2);
    // s3 = s1+s2; //Needs Operator Overloading
    s3.display();
}