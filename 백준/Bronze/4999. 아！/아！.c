#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[1001] = "";
	char str2[1001] = "";
	char* p1 = str1, * p2 = str2;
	int len1, len2;

	gets(str1);
	gets(str2);

	len1 = strlen(str1);
	len2 = strlen(str2);

	if (len1 >= len2)
		printf("go");
	else
		printf("no");

	
	return 0;
}