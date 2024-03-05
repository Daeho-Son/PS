#include <stdio.h>

int		check_prime(int n)
{
	if (n == 1)
		return (0);
	if (n == 2 || n == 3)
		return (1);
	for (int i = 2; i * i <= n; i++)
	{
		if (n % i == 0)
			return (0);
	}
	return (1);
}

int		main(void)
{
	int		N;	// N <= 100
	int		ns;	// number <=1000
	int		count;

	count = 0;
	scanf("%d", &N);
	while (N--)
	{
		scanf("%d", &ns);
		if (check_prime(ns))
			count++;
	}
	printf("%d\n", count);
	return (0);
}
