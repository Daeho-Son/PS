#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int		count;
	int		*weight_table;
	int		*height_table;

	scanf("%d", &count);
	weight_table = (int *)malloc(sizeof(int) * count);
	height_table = (int *)malloc(sizeof(int) * count);
	for (int i = 0; i < count; i++)
	{
		scanf("%d %d", &weight_table[i], &height_table[i]);
	}
	for (int i = 0; i < count; i++)
	{
		printf("index: %d\n", i);
		printf("%d %d\n", weight_table[i], height_table[i]);
	}
	free(weight_table);
	free(height_table);
	return (0);
}
