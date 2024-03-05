#include <stdio.h>

void	swap(int *x, int *y)
{
	int		tmp;

	tmp = *x;
	*x = *y;
	*y = tmp;
}

void	sort(int *a, int *b, int *c)
{
	int		big;

	big = (*a > *b) ? *a : *b;
	big = (big > *c) ? big : *c;
	if (big == *a)
		swap(a, c);
	else if (big == *b)
		swap(b, c);
}

int		main(void)
{
	int		a, b, c;

	while (1)
	{
		scanf("%d %d %d", &a, &b, &c);
		if (a == 0 && b == 0 && c == 0)
			break ;
		sort(&a, &b, &c);
		if ((a * a) + (b * b) == c * c)
			printf("right\n");
		else
			printf("wrong\n");
	}
	return (0);
}
