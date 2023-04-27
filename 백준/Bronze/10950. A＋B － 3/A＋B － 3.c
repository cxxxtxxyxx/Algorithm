#include <stdio.h>

int main(void)
{
	int T, x;
	scanf("%d", &T);
	for(x = 1; x < T + 1; x++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
	return 0;
}