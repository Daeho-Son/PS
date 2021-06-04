#include <stdio.h>

int		main(void)
{
	int	n;
	int	line;
	int	tmp;

	scanf("%d", &n);
	line = 0;
	tmp = 0;
	while (tmp < n)
		tmp += ++line;
	printf("n : %d\nline : %d\ntmp : %d\n", n, line, tmp);
	if (line %2 == 1)
		printf("%d/%d\n", 1 + (tmp - n), line - (tmp - n));
	else
		printf("%d/%d\n", line - (tmp - n), 1 + (tmp - n));
	return (0);
}
