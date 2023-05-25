#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[6] = "";
	char* p = str;
	char* p2 = str;
	int len;
	int cnt = 0;

	gets(str);
	while (strcmp(str, "0") != 0)
	{
		len = strlen(str);
		for (p = str, p2 = str + len - 1; p < str + len / 2; p++, p2--)
		{
			if (*p != *p2)
			{
				printf("no\n");
				cnt++;
				break;
			}
		}
		
		if (cnt == 0)
			printf("yes\n");
		cnt = 0;
		for (p = str; *p; p++)
			*p = '\0';
		gets(str);
	}
	
	return 0;
}