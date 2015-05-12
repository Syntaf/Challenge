section .data

; -----
;   Define standard constants

TRUE				equ	1
FALSE				equ	0

EXIT_SUCCESS        equ 0       ; successful operation
SYS_exit            equ 60      ; call code for terminate

LF                  equ 10
NULL                equ 0
ESC                 equ 27

STDIN               equ 0
STDOUT              equ 1
STDERR              equ 2

SYS_read            equ 0   
SYS_write           equ 1

; -----
;   Local variables

len                 dd  0

; -----
;   Error messages

errReturnVal        db  "Bad byte: '",                  NULL
errReturnValFin     db  "' detected, ending...", LF,    NULL

; -----
;   Formatting variables

space               db  " ",        NULL
newLine             db  LF,         NULL
doubleDigits        db  "Bitey",    NULL

section .bss

; ----------------------------------
;   Uninitialized Static Data Declarations

input               resb    7

; **********************************************

extern getHex, matchByte, printString

section .text
global main
main:

    mov rdi, input          ; store in input var
    call getHex             ; prompt user for hex value
    
    mov dword[len], eax     ; store length into len variable

     mov rbx, 2
     xor r10, r10
     xor r12, r12
     mov r9, input
    
    printBytes:
        
        cmp ebx, 4
        jne skipPrint
            mov rdi, doubleDigits
            call printString
            mov rdi, space
            call printString
        skipPrint 

        mov dil, byte[r9+rbx]
        call matchByte

        cmp rax, TRUE
        je success
            mov rdi, errReturnVal
            call printString
            
            mov rax, r9
            add rax, rbx
            mov rsi, rax
            mov rdx, 1
            mov rax, SYS_write
            mov rdi, STDOUT
            syscall
            
            mov rdi, errReturnValFin
            call printString
            jmp endPrintBytes
        success:

        inc rbx
        cmp ebx, dword[len]
        jge endPrintBytes
        jmp printBytes
    endPrintBytes: 

    mov rdi, newLine
    call printString
    
; **********************************************
;   Done, terminate program

last:
    mov rax, SYS_exit       ; call for exit(SYS_exit)
    mov rbx, EXIT_SUCCESS   ; return code of 0 (no error)
    syscall
