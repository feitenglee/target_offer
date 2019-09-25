/*
 * @Author: lifeiteng@live.com
 * @Github: https://github.com/feitenglee/target_offer
 * @Date: 2019-09-23 19:48:36
 * @LastEditTime: 2019-09-23 19:54:33
 * @Description: 
 * @State: PYTHON35 PASS
 */
#include <iostream>
using namespace std;

class Object{
    void* data;
    const int size;
    const char id;
public:
    Object(int sz, char c):size(sz), id(c){
        data = new char[size];
        cout<<"Constructor"<<id<<",size = "<<size<<endl;
    }
    ~Object(){
        cout<<"Destructor"<<id<<endl;
        delete []data;
    }
};

int main(){
    Object* a = new Object(20,'a');
    delete a;
    // void* b = new Object(20,'b');
    // delete b;
    return 0;
    
}
    
