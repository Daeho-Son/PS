#include <stdio.h>

int	get_factorial(int n)
{
	int		factorial;

	factorial = 1;
	while (n > 0)
		factorial = factorial * n--;
	return (factorial);
}

int	main(void)
{
	int		n;
	int		k;
	int		f_n;
	int		f_k;
	int		f_n_k;

	scanf("%d", &n);
	scanf("%d", &k);
	f_n = get_factorial(n);
	f_k = get_factorial(k);
	f_n_k = get_factorial(n - k);
	printf("%d\n", f_n / (f_k * f_n_k));
	return (0);
}
