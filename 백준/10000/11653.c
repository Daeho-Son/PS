#include <stdio.h>
#include <math.h>

int		main(void)
{
	long long	N;
	long long	i;
	long long	sqrt_n;

	scanf("%lld", &N);
	if (N == 1)
		return (0);
	i = 2;
	sqrt_n = sqrt(N);
	while (i <= sqrt_n)
	{
		if (N % i != 0)
			i++;
		else
		{
			printf("%lld\n", i);
			N = N / i;
		}
	}
	if (N > 1)
		printf("%lld\n", N);
	return (0);
}
