#include <stdio.h>
#include <stdlib.h>

int		counter[8001] = { 0, };

void	arithmetic_mean(int input_count, int min, int max)
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
	printf("%d\n", sum / input_count);
}

void	median_value(int non_same_count, int min, int max)
{
	int		middle;
	int		count;

	middle = non_same_count / 2;
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

void	mode(int input_count, int min, int max)
{
	int		mode;
	int		rank;

	if (input_count == 1)
		printf("%d\n", min);
	mode = -4000;
	for (int i = min; i <= max; i++)
	{
		if (mode < counter[4000 + i])
			mode = counter[4000 + i];
	}
	rank = 0;
	for (int i = min; i <= max; i++)
	{
		if (mode == counter[4000 + i])
			rank++;
		if (rank == 2)
		{
			printf("%d\n", i);
			break ;
		}
	}
}

void difference_between_maximum_minimum(int min, int max)
{
	printf("%d\n", max - min);
}

int	main(void)
{
	int		input_count;
	int		max;
	int		min;
	int		non_same_count;
	int		n;

	non_same_count = 0;
	min = 4000;
	max = -4000;
	scanf("%d", &input_count);
	for (int i = 0; i < input_count; i++)
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
	arithmetic_mean(input_count, min, max);
	median_value(non_same_count, min, max);
	mode(input_count, min, max);
	difference_between_maximum_minimum(min, max);
	return (0);
}