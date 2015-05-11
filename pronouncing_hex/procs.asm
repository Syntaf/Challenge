section .data

; -----
;   Define constants

TRUE        equ 1
FALSE       equ 0

STDIN       equ 0   ; standard input
STDOUT      equ 1   ; standard output
STDERR      equ 2   ; standard error

SYS_read    equ 0   ; code for read
SYS_write   equ 1   ; code for write

LF          equ 10
SPACE       equ " "
NULL        equ 0
ESC         equ 27

; -----
;   Program constants

MAXLEN      equ 6

; -----
;   Variables for procedures

promptInput db  "Enter hex string(formatted as 0x0000): "
            db  LF, NULL

errBadInput db  "Error, bad input provided, re-enter: "
            db  LF, NULL

section .bss

; -----
;   Uninitialized static data

section .text

; -----
;   Call printString(string)

; Arguments:
;   1) string, address - rdi

global  printString
printString:
    push rbp
    mov rbp, rsp
    push rbx
    push rsi
    push rdi
    push rdx

    ; -----
    ; Count characters in string

    mov rbx, rdi
    mov rdx, 0
    strCountLoop:
        cmp byte[rbx], NULL
        je strCountDone
        inc rbx
        inc rdx
        jmp strCountLoop
    strCountDone:

    cmp rdx, 0
    je prtDone

    ; -----
    ; Call OS to output string

    mov rax, SYS_write
    mov rsi, rdi
    mov rdi, STDOUT

    syscall

    prtDone:
    pop rdx
    pop rdi
    pop rsi
    pop rbx
    pop rbp
    ret

; -----
;   call getHex(str)

; Arguments Passed:
;   1) string, addr - rdi

global getHex
getHex:
    push rbx
    mov rbx, rdi

    mov rdi, promptInput    ; prompt user 
    call printString        ; print

    reprompt:
    mov rax, SYS_read       ; read input from user
    mov rdi, STDIN
    mov rsi, rbx
    mov rdx, MAXLEN         ; read only MAXLEN chars
    syscall

    mov r9, rbx             ; get copy of string address
    xor r10, r10            ; clear register for byte comparison
    addNull:
        mov r10b, byte[r9]      ; get byte of string
        cmp r10b, 0x20          ; if byte is a terminating value
        jl doneAddNull          ; end loop, set NULL
        inc r9                  ; other wise move forward one byte
        jmp addNull
    doneAddNull:
    mov byte[r9], NULL      ; set NULL terminated string

    cmp byte[rbx], 0x30     ; ensure first byte is '0'
    je goodByte
        mov rdi, errBadInput    ; print bad input
        call printString
        jmp reprompt            ; re-prompt
    goodByte:
    cmp byte[rbx+1], 0x78   ; ensure second byte is 'x'
    je _goodByte
        mov rdi, errBadInput    ; print bad input
        call printString
        jmp reprompt            ; re-prompt
    _goodByte:
    cmp byte[rbx+2], NULL   ; if there isn't anything after '0x', bad
    jne __goodByte
        mov rdi, errBadInput    ; print bad input
        call printString
        jmp reprompt            ; re-prompt
    __goodByte:
    pop rbx
ret
