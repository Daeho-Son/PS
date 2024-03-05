#include <stdio.h>
#include <stdlib.h>

void	run(int *weight_table, int *height_table, int *rank_table, int count)
{
	for (int i = 0; i < count; i++)
	{
		for (int j = 0; j < count; j++)
		{
			if (i == j)
				continue ;
			if (weight_table[i] < weight_table[j] && \
				height_table[i] < height_table[j])
				rank_table[i]++;
		}
		rank_table[i]++;
	}
}

int	main(void)
{
	int		count;
	int		*weight_table;
	int		*height_table;
	int		*rank_table;

	scanf("%d", &count);
	weight_table = (int *)malloc(sizeof(int) * count);
	height_table = (int *)malloc(sizeof(int) * count);
	rank_table = (int *)calloc(count, sizeof(int));
	for (int i = 0; i < count; i++)
	{
		scanf("%d %d", &weight_table[i], &height_table[i]);
	}
	run(weight_table, height_table, rank_table, count);
	for (int i = 0; i < count; i++)
	{
		printf("%d\n", rank_table[i]);
	}
	free(weight_table);
	free(height_table);
	free(rank_table);
	return (0);
}
