#include <stdio.h>

int main()
{
	int i;               /* Ein ganzzahliger Datentyp */
	printf("Bitte geben Sie eine Zahl ein : ");
	scanf_s("%d", &i);      /* Wartet auf die Eingabe */
	printf("Die Zahl die Sie eingegeben haben war %x\n", i);
	return 0;
}