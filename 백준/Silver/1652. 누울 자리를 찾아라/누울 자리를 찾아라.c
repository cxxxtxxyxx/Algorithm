#include <stdio.h>
#include <string.h>

int main(void)
{
	char room[100][101] = { '\0', };

	int N;
	int row_cnt = 0;
	int row = 0;
	int col_cnt = 0;
	int col = 0;
	
	scanf("%d", &N);
	getchar();

	for (int i = 0; i < N; i++)
		gets(room[i]);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (room[i][j] == '.')
			{
				row_cnt++;
				if (j == N - 1)
				{
					if (row_cnt >= 2)
						row++;
					row_cnt = 0;
				}
			}
			else
			{
				if (row_cnt >= 2)
					row++;
				row_cnt = 0;
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (room[j][i] == '.')
			{
				col_cnt++;
				if (j == N - 1)
				{
					if (col_cnt >= 2)
						col++;
					col_cnt = 0;
				}
			}
			else
			{
				if (col_cnt >= 2)				
					col++;
				col_cnt = 0;
			}
		}
	}

	printf("%d %d", row, col);
	
	return 0;
}