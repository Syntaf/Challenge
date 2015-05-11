all:
	yasm -g dwarf2 -f elf64 procs.asm
	yasm -g dwarf2 -f elf64 main.asm
	gcc -g -o main main.o procs.o
