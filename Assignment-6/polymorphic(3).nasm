global _start  

section .text

_start:  
  
xor eax, eax  
inc eax  
xor ebx, ebx  
int 0x80  
