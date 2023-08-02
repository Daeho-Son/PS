#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K)
{
	priority_queue<int> pq;
	int answer = 0;
	int sum = 0;

	for (auto& i : scoville)
		pq.push(i * (-1));
	while (pq.top() * (-1) < K)
	{
		sum = pq.top() * (-1);
		pq.pop();
		if (pq.empty())
			return (-1);
		sum += pq.top() * (-1) * 2;
		pq.pop();
		pq.push(-sum);
		answer++;
	}
	return answer;
}