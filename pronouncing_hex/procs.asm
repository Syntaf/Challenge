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

space       db  " ", NULL
; -----
;   Hex values specific to program 

A_placeValue        db  "Atta",     NULL
B_placeValue        db  "Bibbity",  NULL
C_placeValue        db  "City",     NULL
D_placeValue        db  "Dickety",  NULL
E_placeValue        db  "Ebbity",   NULL
F_placeValue        db  "Fleventy", NULL
doubleDigits        db  "Bitey",    NULL

; -----
;   Number values in string format
Nine                db  "Nine",     NULL
Eight               db  "Eight",    NULL
Seven               db  "Seven",    NULL
Six                 db  "Six",      NULL
Five                db  "Five",     NULL
Four                db  "Four",     NULL
Three               db  "Three",    NULL
Two                 db  "Two",      NULL
One                 db  "One",      NULL

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
; Returns:
;   length - rax
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
    xor rax, rax
    addNull:
        mov r10b, byte[r9]      ; get byte of string
        cmp r10b, 0x20          ; if byte is a terminating value
        jl doneAddNull          ; end loop, set NULL
        inc r9                  ; other wise move forward one byte
        inc rax
        jmp addNull
    doneAddNull:
    mov byte[r9], NULL          ; set NULL terminated string

    cmp byte[rbx], 0x30         ; ensure first byte is '0'
    je goodByte
        mov rdi, errBadInput    ; print bad input
        call printString
        jmp reprompt            ; re-prompt
    goodByte:
    cmp byte[rbx+1], 0x78       ; ensure second byte is 'x'
    je _goodByte
        mov rdi, errBadInput    ; print bad input
        call printString
        jmp reprompt            ; re-prompt
    _goodByte:
    cmp byte[rbx+2], NULL       ; if there isn't anything after '0x', bad
    jne __goodByte
        mov rdi, errBadInput    ; print bad input
        call printString
        jmp reprompt            ; re-prompt
    __goodByte:
    pop rbx
ret

; -----
;   call matchByte(chr)

; Arguments passed:
;   1) char, value -> rdi 
; Returns:
;   TRUE/FALSE -> rax

global matchByte
matchByte:

    mov r10b, dil
    mov rax, FALSE

    cmp r10b, 0x39                  ; check if lies in possible number range
    jle isNum                       ; skip letter check if so

    cmp r10b, 0x41                  ; 'A'
    jne notA
        mov rdi, A_placeValue
        jmp doPrint
    notA:
    cmp r10b, 0x42                  ; 'B'
    jne notB
        mov rdi, B_placeValue
        jmp doPrint
    notB:
    cmp r10b, 0x43                  ; 'C'
    jne notC
        mov rdi, C_placeValue
        jmp doPrint
    notC:
    cmp r10b, 0x44                  ; 'D'
    jne notD
        mov rdi, D_placeValue
        jmp doPrint
    notD:
    cmp r10b, 0x45                  ; 'E'
    jne notE
        mov rdi, E_placeValue
        jmp doPrint
    notE:
    cmp r10b, 0x46                  ; 'F'
    jne notF
        mov rdi, F_placeValue
        jmp doPrint
    notF:

    jmp fin                         ; no matches, return false

    isNum:
    cmp r10b, 0x30                  ; '0'
    jne notZero
        mov rax, TRUE
        jmp fin
    notZero:     
    cmp r10b, 0x31                  ; '1'
    jne notOne
        mov rdi, One
        jmp doPrint
    notOne:
    cmp r10b, 0x32                  ; '2'
    jne notTwo
        mov rdi, Two 
        jmp doPrint
    notTwo:
    cmp r10b, 0x33                  ; '3'
    jne notThree
        mov rdi, Three
        jmp doPrint
    notThree:
    cmp r10b, 0x34                  ; '4'
    jne notFour
        mov rdi, Four
        jmp doPrint
    notFour:
    cmp r10b, 0x35                  ; '5'
    jne notFive
        mov rdi, Five
        jmp doPrint
    notFive:
    cmp r10b, 0x36                  ; '6'
    jne notSix
        mov rdi, Six
        jmp doPrint
    notSix:
    cmp r10b, 0x37                  ; '7'
    jne notSeven
        mov rdi, Seven
        jmp doPrint
    notSeven:
    cmp r10b, 0x38                  ; '8'
    jne notEight
        mov rdi, Eight
        jmp doPrint
    notEight:
    cmp r10b, 0x39                  ; '9'
    jne notNine
        mov rdi, Nine
        jmp doPrint
    notNine:

    jmp fin

    doPrint:
        call printString
        mov rdi, space
        call printString
        mov rax, TRUE
    fin:
ret

