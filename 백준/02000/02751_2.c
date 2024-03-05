#include <stdio.h>
#include <stdlib.h>

int sorted[2000001] = { 0, };

int main(void)
{
	int count;
	int s_i;

	scanf("%d", &count);
	for (int i = 0; i < count; i++)
	{
		scanf("%d", &s_i);
		sorted[s_i + 1000000] = 1;
	}
	for (int i = 0; i < 2000001; i++)
	{
		if (sorted[i] == 1)
			printf("%d\n", i - 1000000);
	}
	return (0);
}