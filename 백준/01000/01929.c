#include <stdio.h>
#include <stdlib.h>

int		main(void)
{
	int		tmp[1000001] = {1, 1};
	int		M, N;
	int		count;

	scanf("%d %d", &M, &N);
	// input number
	for (int i = 2; i * i <= N; i++)
	{ 
		if (!tmp[i])
		{
			for (int j = i * i; j <= N; j += i)
				tmp[j] = 1;
		}
	}
	// print
	count = 0;
	for (int i = M; i <= N; i++)
	{
		if (tmp[i] == 0)
		{
			printf("%d\n", i);
			count++;
		}
	}
	printf("count: %d\n", count);
	return (0);
}
