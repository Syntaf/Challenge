section .data

; -----
;		Define standard constants

TRUE				equ	1
FALSE				equ	0

EXIT_SUCCESS        equ 0       ; successful operation
SYS_exit            equ 60      ; call code for terminate

; -----
;		Local variables

section .bss

; ----------------------------------
;		Uninitialized Static Data Declarations

input               resb    7

; **********************************************

extern getHex

section .text
global main
main:

    mov rdi, input          ; store in input var
    call getHex             ; prompt user for hex value

; **********************************************
;   Done, terminate program

last:
    mov rax, SYS_exit       ; call for exit(SYS_exit)
    mov rbx, EXIT_SUCCESS   ; return code of 0 (no error)
    syscall
