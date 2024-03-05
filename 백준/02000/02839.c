#include <stdio.h>
#include <limits.h>

int		get_count(int N)
{
	for (int f_count = N / 5; f_count >= 0; f_count--)
	{
		if ((N - 5 * f_count) % 3 == 0)
			return (f_count + (N - 5 * f_count) / 3);
	}
	return (-1);
}
int		main(void)
{
	int		N;
	
	scanf("%d", &N);
	printf("%d\n", get_count(N));
	return (0);
}
