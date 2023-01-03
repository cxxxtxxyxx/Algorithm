#include <stdio.h>

int main(void)
{
	int x, n;
	int y= 0;
	scanf("%d",&n);
	for(x = 1; x <= n; x++)
	{
		y += x;
	}
	printf("%d", y);
	return 0;
}