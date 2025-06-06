# Compile the shared library libdars.so from dars.c and roesset_quake.c
# This Makefile is designed to work with the MinGW-w64 toolchain for Windows.
# To use this Makefile, ensure you have the MinGW-w64 toolchain installed
# and available in your PATH,
# /usr/i686-w64-mingw32/bin for 32-bit Windows compilation or
# /usr/x86_64-w64-mingw32/bin for 64-bit Windows compilation.
# Uncomment the appropriate CC line below based on your architecture.
#CC=/usr/bin/i686-w64-mingw32-gcc # For 32-bit Windows compilation
#CC=/usr/bin/x86_64-w64-mingw32-gcc # For 64-bit Windows compilation
CC=gcc     # For native compilation on Linux
#CFLAGS=-ggdb -O0 -Wall
CFLAGS= -O3 -Wall
CPPFLAGS=
LDFLAGS=

all: libdars.so test 

libdars.so: dars.o roesset_quake.o
	$(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) \
		-shared -fPIC -o libdars.so dars.o roesset_quake.o

dars.o: dars.c
	$(CC) -c dars.c

roesset_quake.o: roesset_quake.c
	$(CC) -c roesset_quake.c

test: libdars.so dars.h test.c
	$(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) -o test test.c ./libdars.so -lm

clean:
	rm *.o libdars.so

