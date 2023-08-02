#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void remove_dup(vector<int>& lost, vector<int>& reserve) {
    int i = 0;
    int j = 0;

    while (1) {
        if (i == lost.size() || j == reserve.size())
            break;
        if (lost[i] < reserve[j])
            i++;
        else if (reserve[j] < lost[i])
            j++;
        else
        {
            lost.erase(lost.begin() + i);
            reserve.erase(reserve.begin() + j);
        }
    }
}

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int temp_i;
    
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    remove_dup(lost, reserve);
    for (int i = 0; i < lost.size(); i++) {
        for (int j = 0; j < reserve.size(); j++) {
            if (reserve[j] < lost[i] - 1)
                continue;
            if (lost[i] + 1 < reserve[j])
                break;
            if (lost[i] - 1 <= reserve[j] && reserve[j] <= lost[i] + 1) {
                lost.erase(lost.begin() + i);
                reserve.erase(reserve.begin() + j);
                i--;
                break;
            }
        }
    }
    return n - lost.size();
}