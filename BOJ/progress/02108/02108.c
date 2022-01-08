#include <stdio.h>
#include <stdlib.h>

int		counter[8001] = { 0, };

void	arithmetic_mean(int N, int min, int max)
{
	int		sum;

	sum = 0;
	for (int i = min; i <= max; i++)
	{
		if (counter[4000 + i] != 0)
			sum = sum + (i * counter[4000 + i]);
	}
	if (sum < 0)
		--sum;
	printf("%d\n", sum / N);
}

void	median_value(int N, int min, int max)
{
	int		middle;
	int		count;

	middle = N / 2;
	count = -1;
	for (int i = min; i <= max; i++)
	{
		if (counter[4000 + i] != 0)
			count++;
		if (count == middle)
		{
			printf("%d\n", i);
			break ;
		}
	}
}

int	main(void)
{
	int		N;
	int		n;
	int		max;
	int		min;
	int		non_same_count;

	non_same_count = 0;
	min = 4000;
	max = -4000;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &n);
		if (counter[4000 + n] == 0)
			non_same_count++;
		counter[4000 + n]++;
		if (n < min)
			min = n;
		if (max < n)
			max = n;
	}
	arithmetic_mean(N, min, max);
	median_value(non_same_count, min, max);
	return (0);
}