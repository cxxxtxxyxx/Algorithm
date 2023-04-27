#include <stdio.h>

int main(void)
{
	int i, u, x, y, N;
	scanf("%d", &N);
	for(i = 1; i <= N; i++)
	{
		for(x = 1; x <= i; x++)
		{
			printf("*");
		}
		printf("\n");
	}
	for(u = N - 1; u > 0; u--)
	{
		for(y = u; y > 0; y--)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}