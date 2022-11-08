#include <stdio.h>
#include <string.h>

int main(void)
{
	int N;
	char str[1001] = "";
	char* p = str;
	char* p2 = str;
	int len;

	scanf("%d", &N);
	getchar();
	for (int i = 0; i < N; i++)
	{
		gets(str);
		len = strlen(str);

		for (p = str; *p; p++)
			if (*p == ' ')
				*p = '\0';

		for (p = str; p < str + len; p++)
		{
			if (*p == '\0')
				printf(" ");
			else 
			{
				for (p2 = p + strlen(p) - 1; p2 >= p; p2--)
					printf("%c", *p2);
				p += strlen(p) - 1;
			}
		}

		printf("\n");

		for (p = str; p < str + len; p++)
			*p = '\0';
	}


	
	return 0;
}