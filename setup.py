from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(
    name='dvars',
    version='0.1',
    description='Response spectrum calculation for earthquake engineering',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pavel Zacherle',
    #author_email='zapa@ipe.muni.cz',
    keywords='response spectrum, earthquake engineering',
    license='Public Domain',
    #url='https://gist.github.com/zacherle/',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: End Users/Desktop',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
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
        'dvars.dars':['libdars.so'],
    },

)

