/*
 * @Author: lifeiteng@live.com
 * @Github: https://github.com/feitenglee/target_offer
 * @Date: 2019-09-03 09:35:22
 * @LastEditTime: 2019-09-03 09:35:22
 * @Description: 
 * @State: PYTHON35 PASS
 */
class Solution {
public:
    vector<vector<int>> p;
    vector<int> s;
    //unordered_set<int> used;
    
    vector<vector<int>> permute(vector<int>& nums) {
        dfs(0, nums);
        return p;
    }
    
    void dfs(int n, vector<int>& nums){
        if(n == nums.size()){
            p.push_back(s);
            return;
        }

        for(int i = 0; i < nums.size() ; i++){
            if(find(s.begin(),s.end(),nums[i]) == s.end()){
                s.push_back(nums[i]);
                dfs(n+1,nums);
                //回溯
                s.pop_back();
            }
        }
    }
};