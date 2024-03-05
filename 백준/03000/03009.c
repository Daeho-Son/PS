#include <stdio.h>

int		main(void)
{
	int		x1, y1;
	int		x2, y2;
	int		x3, y3;

	scanf("%d %d", &x1, &y1);
	scanf("%d %d", &x2, &y2);
	scanf("%d %d", &x3, &y3);
	printf("%d %d", x1 ^ x2 ^ x3, y1 ^ y2 ^ y3);
	return (0);
}
