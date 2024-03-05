#include <stdio.h>

int	main(void)
{
	int		input1;
	int		input2;
	int		common;
	int		divide_number;

	scanf("%d %d", &input1, &input2);
	common = 1;
	divide_number = 2;
	while (1)
	{
		if (input1 < divide_number || input2 < divide_number)
			break ;
		if (input1 % divide_number == 0 && input2 % divide_number == 0)
		{
			common *= divide_number;
			input1 /= divide_number;
			input2 /= divide_number;
			divide_number = 2;
		}
		else
			divide_number++;
	}
	printf("%d\n", common);
	printf("%d\n", common * input1 * input2);
	return (0);
}
