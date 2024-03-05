#include <stdio.h>
#include <stdlib.h>

int counting[10001] = {	0, };

int main(void)
{
	int num_of_numbers;
	int n;
	int max;
	int min;

	max = 0;
	min = 10000;
	scanf("%d", &num_of_numbers);
	for (int i = 0; i < num_of_numbers; i++)
	{
		scanf("%d", &n);
		if (max < n)
			max = n;
		if (n < min)
			min = n;
		counting[n]++;
	}
	for (int i = min; i <= max; i++)
	{
		for (int j = 0; j < counting[i]; j++)
			printf("%d\n", i);
	}
	return (0);
}