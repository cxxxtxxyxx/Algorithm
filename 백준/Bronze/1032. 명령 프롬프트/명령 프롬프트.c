#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[50][51] = { '\0', };
	char newstr[51] = "";
	char* p = newstr;
	int N;
	int len, cnt = 0;
	char* pc[50] = { NULL, };
	int i, j;

	scanf("%d", &N);
	getchar();
	for (i = 0; i < N; i++)
	{
		scanf("%s", str[i]);
		getchar();
	}

	len = strlen(str[0]);

	for (i = 0; i < len; i++)
	{
		for (j = 0; j < N; j++)
		{
			if (str[0][i] == str[j][i])
				cnt++;
			
		}
		if (cnt == N)
			*(p++) = str[0][i];
		else
			*(p++) = '?';

		cnt = 0;
	}
	printf("%s", newstr);


	return 0;
}