import os
import subprocess
from setuptools import setup, find_packages

import sys

plat_name = ''
if '--plat-name' in sys.argv:
    index = sys.argv.index('--plat-name')
    if index + 1 < len(sys.argv):
        plat_name = sys.argv[index + 1]
        print(f"Platform name: {plat_name}")
    else:
        raise ValueError("No platform name provided after '--plat-name'.")

if plat_name in ['win-amd64','win_amd64','win32']:
    # cross-build
    # Windows shared library extension
    lib_extension = '.so'   #'.pyd'
else:
    # native build
    # Unix standard shared library extension
    lib_extension = '.so'

lib_name = 'libdars' + lib_extension

with open('README.md') as f:
    long_description = ''.join(f.readlines())

# Ensure the Makefile exists in the libsrc directory
makefile_path = 'libsrc/Makefile'
if not os.path.exists(makefile_path):
    raise FileNotFoundError("Makefile not found at "+makefile_path+". Please ensure it exists in the libsrc directory.")
# Build the shared library
try:
    subprocess.run(['make', '-C', 'libsrc', 'PLAT='+plat_name], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during building the shared library: {e}")
    print("Make sure you have 'make' installed and the Makefile is correctly configured.")
    raise
# Check if the shared library was built successfully
lib_path = os.path.join('libsrc', lib_name)
if not os.path.exists(lib_path):
    raise FileNotFoundError("Shared library not found at "+lib_path+". Please ensure it was built successfully.")
# Install the shared library to the package directory dvars/dars
try:
    subprocess.run(['make', '-C', 'libsrc', 'install', 'PLAT='+plat_name], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during installing the shared library: {e}")
    print("Make sure you have 'make' installed and the Makefile is correctly configured.")
    raise

setup(
    name='dvars',
    version='0.1.1',
    description = "Response spectra calculations for earthquake engineering.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pavel Zacherle',
    author_email='zapa@ipe.muni.cz',
    keywords = ["response spectra", "earthquake engineering"],
    license='Open Source',
    url='https://github.com/zacherle/dvars',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: C',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        ],
    zip_safe=False,
    python_requires='>=3.8',
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    extras_require={
        'testing': ['pytest'],
    },
    # https://stackoverflow.com/questions/24347450/how-do-you-add-additional-files-to-a-wheel
    include_package_data=True,     # MANIFEST.in to sdist
    package_data={
        'dvars.dars':[lib_name],
    },

)
