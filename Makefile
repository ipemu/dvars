# Makefile for building the dvars package on Linux.
# It allows native build for Linux and cross-build for Windows (32-bit and 64-bit).
# The package is structured to include a C extension located in the `libsrc` directory, which is compiled during the build process.
# The Makefile assumes that the necessary build tools are installed on the system, such as Python, setuptools, and a C compiler.

.PHONY: clean build buildw32 buildw64 distclean 

# default target is to build the package for the current platform
default: build
#
# linux native build
build:
	python3 setup.py sdist bdist_wheel

# buildw32 is for 32-bit Windows builds
buildw32:
	make -C libsrc clean
	python3 setup.py sdist bdist_wheel --plat-name win32

# buildw64 is for 64-bit Windows builds
buildw64:
	make -C libsrc clean
	python3 setup.py sdist bdist_wheel --plat-name win-amd64

# clean removes build artifacts
clean:
	make -C libsrc clean
	-rm -r dvars.egg-info
	-rm -r build/lib
	-rm dvars/dars/libdars.so
	#-rm dvars/dars/libdars.pyd

# distclean removes all build artifacts and cleated distribution files
distclean:
	make -C libsrc clean
	-rm -r dvars.egg-info
	-rm -r build/lib
	-rm dvars/dars/libdars.so
	#-rm dvars/dars/libdars.pyd
	-rm -r dist

