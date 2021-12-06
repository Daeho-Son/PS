#include <stdio.h>
#include <string.h>

int	get_constructor(int n)
{
	int		result;

	result = n;
	while (n >= 10)
	{
		result += (n % 10);
		n /= 10;
	}
	result += n;
	return (result);
}

int	get_min(int *ns)
{
	int		i;
	int		min;

	min = ns[0];
	i = 0;
	while (ns[++i] != 0)
	{
		if (ns[i] < min)
			min = ns[i];
	}
	return (min);
}

int	main(void)
{
	int		n;
	int		i;
	int		constructors[100];
	int		constructor;
	int		c_i;

	scanf("%d", &n);
	i = -1;
	c_i = -1;
	memset(&constructors, 0, 100);
	constructor = 0;
	while (constructor <= 1000000)
	{
		constructor = get_constructor(++i);
		if (n == constructor)
			constructors[++c_i] = i;
	}
	if (constructors[0] == 0)
		printf("0\n");
	else
		printf("%d\n", get_min(constructors));
	return (0);
}
