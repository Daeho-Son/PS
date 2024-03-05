#include <stdio.h>

int		main(void)
{
	int	a, b, c;
	int	bep;

	scanf("%d %d %d", &a, &b, &c);
	bep = a / (c - b) + 1;
	if (b >= c)
		printf("-1\n");
	else
		printf("%d\n", bep);
	return (0);
}
