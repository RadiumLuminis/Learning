#include <stdio.h>
#include <iostream>
using namespace std;


int main()
{
	char i;               /* Ein ganzzahliger Datentyp */
	printf("Bitte geben Sie ein Zeichen ein: ");
	scanf_s("%c", &i);      /* Wartet auf die Eingabe */
	int a = (int)i;
	printf("Das Zeichen die Sie eingegeben haben war %c\n", a);
	printf("Das Zeichen als Dezimaler Ascii-Wert: %d\n", a);
	printf("Das Zeichen als Hexadezimaler Wert: %x\n", a);

	char i2;
	cout << "Bitte geben Sie ein weiteres Zeichen ein: ";
	cin >> i2;
	cout << "Ihre Eingabe: " << i2 << endl;
	cout << "Als Dezimaler Wert: " << (int)i2 << endl;
	cout << "Als Hexadezimaler-Wert: " << hex << (int)i2 << endl;

	return 0;
}