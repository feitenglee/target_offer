/*
 * @Author: lifeiteng@live.com
 * @Github: https://github.com/feitenglee/target_offer
 * @Date: 2019-09-23 19:14:55
 * @LastEditTime: 2019-09-23 19:14:55
 * @Description: 
 * @State: PYTHON35 PASS
 */
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    int n;
    cin >>n;
    cout <<"There are " <<n <<" lines." <<endl;
    getchar();

    string s;
    int lineNum = 0;
    while (!cin.eof()){
        getline(cin, s);
        stringstream ss(s);

        lineNum += 1;
        while(getline(ss, s, ' ')){
            if (lineNum ==1 || lineNum >= 4){
                cout <<"Line " <<lineNum <<": string \"" <<s <<"\"\n";
            }else if (lineNum == 2){
                cout <<"Line " <<lineNum <<": float " <<stof(s) <<endl;
            }else{
                cout <<"Line " <<lineNum <<": integer " <<stoi(s) <<endl;
            }
        }
    }
    return 0;
}