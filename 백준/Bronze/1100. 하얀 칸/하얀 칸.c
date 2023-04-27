#include <stdio.h>

int main(void)
{
	char chess[8][9] = { '\0', };

	for (int i = 0; i < 8; i++)
	{
		scanf("%s", chess[i]);
		getchar();
	}

	int cnt = 0;

	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if (i % 2 == 0 && j % 2 == 0)
			{
				if (chess[i][j] == 'F')
					cnt++;
			}
			if(i % 2 == 1 && j % 2 == 1)
				if (chess[i][j] == 'F')
					cnt++;

		}
	}

	printf("%d", cnt);
	return 0;
}