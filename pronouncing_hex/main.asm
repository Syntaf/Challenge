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

    mov rbx, 2              ; begin after the '0x'
    xor r10, r10            ; clear r10 for storing byte
    mov r9, input           ; move address of input into r9
    
    printBytes:
        
        cmp ebx, 4                      ; first compare if we have more than two digits
        jne skipPrint
            mov rdi, doubleDigits       ; if so print 'bitey' 
            call printString
            mov rdi, space              ; print ' '
            call printString
        skipPrint 

        mov dil, byte[r9+rbx]           ; get byte
        call matchByte                  ; print corresponding string
    
        cmp rax, TRUE                   ; if function successful
        je success                      ; skip
            mov rdi, errReturnVal       ; else print error string
            call printString
            
            mov rax, r9                 ; print out byte that caused FALSE
            add rax, rbx
            mov rsi, rax
            mov rdx, 1
            mov rax, SYS_write
            mov rdi, STDOUT
            syscall
            
            mov rdi, errReturnValFin    ; print out last part of error string
            call printString
            jmp endPrintBytes
        success:

        inc rbx                         ; increment count
        cmp ebx, dword[len]             ; ensure count is within length
        jge endPrintBytes
        jmp printBytes
    endPrintBytes: 

    mov rdi, newLine        ; end program with newline print
    call printString
    
; **********************************************
;   Done, terminate program

last:
    mov rax, SYS_exit       ; call for exit(SYS_exit)
    mov rbx, EXIT_SUCCESS   ; return code of 0 (no error)
    syscall
