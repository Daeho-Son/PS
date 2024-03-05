#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void	run(int N)
{
	int		number;
	int		rank;

	number = 0;
	rank = 0;
	while (1)
	{
		for (int i = number; i >= 666; i /= 10)
		{
			if (i % 1000 == 666)
			{
				rank++;
				break ;
			}
		}
		if (rank == N)
		{
			printf("%d\n", number);
			return;
		}
		number++;
	}
}

int	main(void)
{
	int		N;

	scanf("%d", &N);
	run(N);
	return (0);
}
