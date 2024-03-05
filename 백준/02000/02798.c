#include <stdio.h>
#include <stdlib.h>

int	get_number(int num_of_input, int m, int *inputs)
{
	int		near;
	int		sum;

	near = 0;
	for (int i = 0; i < num_of_input; i++)
	{
		for (int j = i + 1; j < num_of_input; j++)
		{
			for (int k = j + 1; k < num_of_input; k++)
			{
				sum = inputs[i] + inputs[j] + inputs[k];
				if (sum <= m && near < sum)
					near = sum;
			}
		}
	}
	return (near);
}

int	main(void)
{
	int		num_of_input;
	int		m;
	int		*inputs;

	scanf("%d", &num_of_input);
	scanf("%d", &m);
	inputs = (int *)calloc(num_of_input, sizeof(int));
	for (int i = 0; i < num_of_input; i++)
		scanf("%d", &inputs[i]);
	printf("%d\n", get_number(num_of_input, m, inputs));
	free(inputs);
	return (0);
}
