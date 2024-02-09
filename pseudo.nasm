; if RAM[1] == RAM[0] || RAM[1] > 0:
;     RAM[2] = 1
; RAM[3] = 2


leaw $2, %A
movw %A, %D
leaw $3, %A
movw %D, (%A)

leaw $0, %A
movw (%A), %D
leaw $1, %A
movw (%A), %A
subw %D, %A, %D
leaw $IF, %A
je %D
nop

leaw $1, %A
movw (%A), %D
leaw $IF, %A
jg %D
nop

leaw $end, %A
jmp
nop

leaw $0, %A
movw %A, %D
leaw $2, %A
movw %D, (%A)
leaw $end, %A
jmp
nop

IF:
leaw $1, %A
movw %A, %D
leaw $2, %A
movw %D, (%A)

end:
