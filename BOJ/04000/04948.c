#include <stdio.h>

int main(void)
{
	char ns[246913] = {0};
	int	prime[123456];
	long long i, j, p_index;
	int n;
	int	count;

	p_index = 0;
	for (i = 2; i <= 246912; i++)
	{
		if (!ns[i])
		{
			prime[p_index++] = i;
			for (j = i * i; j <= 246912; j += i)
				ns[j] = 1;
		}
	}
	scanf("%d", &n);
	while (n)
	{
		p_index = 0;
		count = 0;
		while (prime[p_index] <= 2 * n)
		{
			if (prime[p_index] > n)
				count++;
			p_index++;
		}
		printf("%d\n", count);
		scanf("%d", &n);
	}
	return (0);
}
