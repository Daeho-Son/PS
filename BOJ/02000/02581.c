#include <stdio.h>
#include <math.h>
#include <limits.h>

int		check_prime(int n)
{
	if (n == 1)
		return (0);
	if (n == 2 || n == 3)
		return (n);
	for (int i = 2; i <= sqrt(n); i++)
	{
		if (n % i == 0)
			return (0);
	}
	return (n);
}

int		main(void)
{
	int		M, N;
	int		min, sum;
	int		tmp;

	scanf("%d %d", &M, &N);
	min = INT_MAX;
	sum = 0;
	for (int n = M; n <= N; n++)
	{
		tmp = check_prime(n);
		if (tmp)
			min = (min < tmp) ? min : tmp;
		sum += tmp;
	}
	if (!sum)
	{
		printf("-1\n");
		return (0);
	}
	printf("%d\n", sum);
	printf("%d\n", min);
	return (0);
}
