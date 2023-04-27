#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char str1[101] = "";
	char* p = str1;
	char* p2 = str1;
	char* index = str1;
	int sum = 0;
	scanf("%s", str1);
	
	for (p = str1; *p; p++)
	{
		if (p == str1)
		{
			sum += atoi(p);
			while ('0' <= *p && *p <= '9')
				p++;
			p--;
		}
		else {
			if (*p == '-')
			{
				for (p2 = p + 1; *p2 != '-' && *p2; p2++);
				index = p2 - 1;
				for (p2 = p + 1; p2 <= index; p2++)
				{
					if (*p2 != '+')
					{
						sum -= atoi(p2);
						while ('0' <= *p2 && *p2 <= '9')
							p2++;
						p2--;
					}
				}

				p = index;
			}
			if (*p == '+')
			{
				sum += atoi(p);
				p++;
				while ('0' <= *p && *p <= '9')
					p++;
				p--;
			}
		}
	}
	printf("%d", sum);

	return 0;
}