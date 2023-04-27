#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[501] = "";
	char trans[501] = "";
	char* p = str;
	char* p2 = trans;
	int len;

	gets(str);

	while (strcmp(str, "END") != 0)
	{
		len = strlen(str);
		for (p = str + len - 1, p2 = trans; p >= str; p--, p2++)
			*p2 = *p;

		puts(trans);
		for (p = trans; *p; p++)
			*p = '\0';

		for (p = str; *p; p++)
			*p = '\0';
		gets(str);
	}

	
	return 0;
}