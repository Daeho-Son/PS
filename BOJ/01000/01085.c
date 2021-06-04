#include <stdio.h>

int		main(void)
{
	int		x, y;
	int		w, h;
	int		min_x;
	int		min_y;
	int		min;

	scanf("%d %d", &x, &y);
	scanf("%d %d", &w, &h);
	min_x = (w - x < x) ? (w - x) : x;
	min_y = (h - y < y) ? (h - y) : y;
	min = (min_x < min_y) ? min_x : min_y;
	printf("%d\n", min);
	return(0);
}
