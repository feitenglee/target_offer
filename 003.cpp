/*
 * @Author: lifeiteng@live.com
 * @Github: https://github.com/feitenglee/target_offer
 * @Date: 2019-09-17 20:59:54
 * @LastEditTime: 2019-09-17 21:08:08
 * @Description: 
 * @State: PYTHON35 PASS
 */
#include<iostream>
using namespace std;

int main(){
    long long sum = 0,n;
    int ta,tb,tc,td;
    cin>>ta>>tb>>tc>>td>>n;
    for (int i =5;i<=n;i++){
        sum = td + tb + ta;
        ta = tb;
        tb = tc;
        tc = td;
        td = sum;
        if(sum)
    }
    cout<<sum%1000000007<<endl;
    return 0;
}