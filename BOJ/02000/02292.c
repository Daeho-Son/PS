#include <stdio.h>

int		main(void)
{
	int	n;
	int	count;
	int	result;

	scanf("%d", &n);
	count = 0;
	result = 1;
	if (n == 1)
	{
		printf("1");
		return (0);
	}
	while (result < n)
	{
		result += (6 * count);
		count++;
	}
	printf("%d\n", count);
	return (0);
}
