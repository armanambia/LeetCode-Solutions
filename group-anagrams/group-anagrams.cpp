class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> mp;
        int n=strs.size();
        vector<vector<string>> v;
        for(int i=0;i<n;i++){
            string s=strs[i];
            sort(s.begin(),s.end());
            mp[s].push_back(strs[i]);
        }
        for(auto a:mp){
            std::cout << a.first;
            std::cout << ": ";
            for (auto b: a.second){
                std::cout << b << ", ";
            }
            std::cout << "\n";
        }
        for(auto a:mp){
            vector<string> temp=a.second;
            v.push_back(temp);
        }
        return v;
    }
};