#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long	get_hashing_number(char *s, int r, long long M)
{
	long long	hashing_number;
	long long	pow_n;

	hashing_number = 0;
	for (int i = 0; s[i]; i++)
	{
		pow_n = 1;
		for (int j = 1; j <= i; j++)
		{
			pow_n *= r;
			pow_n %= M;
		}
		hashing_number = ((hashing_number + (s[i] - 'a' + 1) * pow_n) % M);
	}
	return (hashing_number);
}

int	main(void)
{
	int		len;
	char	*s;
	int		r = 31;
	long long	M = 1234567891;

	scanf("%d", &len);
	s = (char *)calloc(len + 1, sizeof(char));
	if (!s)
		return (0);
	scanf("%s", s);
	printf("%lld\n", get_hashing_number(s, r, M));
	free(s);
	return (0);
}
