#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[2501] = "";
	char str2[2501] = "";
	int len1, len2, cnt = 0;
	char* p1 = str1, * p2 = str2;

	gets(str1);
	gets(str2);

	len1 = strlen(str1);
	len2 = strlen(str2);

	for (p1 = str1; *p1; p1++)
	{
		if (strncmp(p1, p2, len2) == 0)
		{
			cnt++;
			p1 += strlen(p2) - 1;
		}
	}

	printf("%d", cnt);

	
	return 0;
}