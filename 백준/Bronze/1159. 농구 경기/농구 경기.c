#include <stdio.h>
#include <string.h>

int main(void)
{
	char name[150][31] = { '\0', };
	char totalname[27] = "";
	char* p = totalname;
	char first_name = 'a';
	int cnt = 0;
	int total_cnt = 0;

	int N;
	scanf("%d", &N);
	getchar();

	for (int i = 0; i < N; i++)
		gets(name[i]);

	for (first_name = 'a'; first_name <= 'z'; first_name++)
	{
		for (int j = 0; j < N; j++)
		{
			if (first_name == name[j][0])
				cnt++;
		}

		if (cnt >= 5)
		{
			*p = first_name;
			p++;
			total_cnt++;
		}

		cnt = 0;

	}

	if (total_cnt == 0)
	{
		printf("PREDAJA");
		return 0;
	}
	else
		printf("%s", totalname);

	
	return 0;
}