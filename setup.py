from setuptools import setup

setup(
        package_data={
            'dvars.dars': ['libdars*.so', 'libdars*.pyd', 'libdars*.dll'],
            },
        ext_package='dvars.dars',
        )
