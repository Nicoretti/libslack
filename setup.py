from setuptools import setup, find_packages

MAJOR_VERSION = 0
MINOR_VERSION = 6
PATCH_VERSION = 1

VERSION_TEMPLATE = '{major}.{minor}.{patch}'

setup(
    name='libslack',
    version=VERSION_TEMPLATE.format(major=MAJOR_VERSION, minor=MINOR_VERSION, patch=PATCH_VERSION),
    packages=find_packages(),
    install_requires=['docopt'],
    url='https://github.com/Nicoretti/libslack',
    license='BSD',
    author='Nicola Coretti',
    author_email='nico.coretti@gmail.com',
    description='A lightweight wrapper around the slack web API.',
    package_data={
        '.': ['**/*.rst']
    },
    entry_points={
        'console_scripts': [
            'scmd=scmd:main',
            'sls=sls:main',
        ],
    },
    keywords=['slack', 'cmd', 'api', 'shell'],
)

