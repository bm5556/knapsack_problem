//0-1 knapsack ploblem
#include <bits/stdc++.h>
#define REP(i,a,b) for(int i=a;i<b;i++)
using namespace std;


int find_max_value(int the_number_of_items, int max_weight, vector<int> Weights, vector<int> Values, bool show_DP=false) {
    vector<int> v(max_weight+1, 0);
    vector<vector<int>> DP(the_number_of_items, v);
    REP(i, 0, the_number_of_items) {
        int current_weight = Weights[i];
        int current_value = Values[i];
        
        DP[i] = (i > 0)? DP[i-1]: v;
        if(current_weight > max_weight) continue;
        else {
            int extra_weight = max_weight - current_weight;
            vector<int> Previous_DP = DP[i];
            REP(j, 0, extra_weight+1) {
                DP[i][j+current_weight] \
                    = max(Previous_DP[j] + current_value, Previous_DP[j+current_weight]);
            }
        }
    }

    if (show_DP) {
        cout << "\n\n";
        for(auto vec: DP) {
            for(int n:vec) cout << n << ' '; 
            cout << endl;
        }
        cout << endl;
    }


    int res = DP[the_number_of_items-1][max_weight];
    return res;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> W, V; int w, v;
    REP(i, 0, N) {
        cin >> w >> v;
        W.push_back(w); V.push_back(v);
    }
    cout << find_max_value(N, K, W, V, true); 
// if you want to show DP, write find_max_value(N, K, W, V, true);
    return 0;
}