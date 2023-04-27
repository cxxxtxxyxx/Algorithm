#include <stdio.h>

int main(void)
{
	char str1[101] = "";
	char* p = str1;
	char str2[101] = "";
	char* p2 = str2;

	scanf("%s", str1);
	
	for (p = str1; *p; p++)
		if ('A' <= *p && *p <= 'Z')
			*(p2++) = *p;

	printf("%s", str2);
	return 0;
}