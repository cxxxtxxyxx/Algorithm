#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[51] = "";
	char str2[51] = "";
	char* p1 = str1, * p2 = str2, * p3 = str1;
	int len1, len2;
	int cnt = 0;
	int min;

	scanf("%s %s", str1, str2);

	len1 = strlen(str1);
	len2 = strlen(str2);
	
	min = len1;

	for (p2 = str2; p2 < str2 + len2 - len1 + 1; p2++)
	{
		for (p1 = str1, p3 = p2; *p1; p1++, p3++)
			if (*p1 != *p3)
				cnt++;
		if (min > cnt)
			min = cnt;
		cnt = 0;
	}

	printf("%d", min);
	return 0;
}