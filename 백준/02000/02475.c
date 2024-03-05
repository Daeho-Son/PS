#include <stdio.h>

int	main(void)
{
	int		ns[5];
	int		square_sum;

	square_sum = 0;
	for (int i = 0; i < 5; i++)
	{
		scanf("%d", &ns[i]);
		square_sum += ns[i] * ns[i];
	}
	printf("%d\n", square_sum % 10);
}
