#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[101] = "";
	char* p = str;

	char cpy[10][11] = { '\0', };
	int cnt = 0;
	int len;
	int L;

	scanf("%s", str);
	len = strlen(str);
	L = len / 10;

	p = str;
	for (int i = 0; i < L; i++)
	{
		strncpy(cpy[cnt++], p, 10);
		p += 10;
	}
	strcpy(cpy[cnt++], p);

	for (int i = 0; i < cnt; i++)
		printf("%s\n", cpy[i]);

	
	return 0;
}