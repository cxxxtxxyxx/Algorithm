#include <stdio.h>

int main(void)
{
	int i, j, N;
	scanf("%d", &N);
	for(i = 1; i <= 2 * N - 1; i++) 
	{
		if((i == 1) || (i == 2 * N - 1))
		{
			for(j = 1; j <= 2 * N - 1; j++)
			{
				printf("*");
			}
			printf("\n");
		}
		else if((i > 1) && (i < N))
		{
			for(j = 1; j < i; j ++)
			{
				printf(" ");
			}
			for(j = 2 * N - 2 * i + 1; j > 0; j--)
			{
				printf("*");
			}
			printf("\n");
		}
		else if(i == N)
		{
			for(j = 1; j < N; j++)
			{
				printf(" ");
			}
			printf("*");
			printf("\n");
		}
		else
		{
			for(j = 2 * N - i; j > 1; j--)
			{
				printf(" ");
			}
			for(j = 1; j < 2 * i - 2 * N + 2; j++)
			{
				printf("*");
			}
			printf("\n");
		}
	}
	return 0;
}