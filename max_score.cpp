/*
 * @Author: lifeiteng@live.com
 * @Github: https://github.com/feitenglee/target_offer
 * @Date: 2019-09-17 20:15:18
 * @LastEditTime: 2019-09-17 20:26:20
 * @Description: 
 * @State: PYTHON35 PASS
 */
#include <iostream>

using namespace std;

int main(){
    int n,m,count = 0;
    int a[1001];
    cin>>n>>m;
    for (int i = 1; i <= n; i++){
        a[i] = 0;
    }
    for (int i = 1,s,e; i <= n; i++){
        cin>>s>>e;
        for (int j = s; j <= e; j++){
            a[j] = 1;
        }
    }
    for (int i = 0,p; i < m; i++){
        cin>>p;
        if (a[p] == 1)
            count ++;
    }
    cout<<count<<endl;
    return 0;
}