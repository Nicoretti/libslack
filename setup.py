from setuptools import setup

setup(
    name='libslack',
    version='0.1.1',
    packages=['', 'tests'],
    install_requires=['docopt'],
    url='https://github.com/Nicoretti/libslack',
    license='BSD',
    author='Nicola Coretti',
    author_email='nico.coretti@gmail.com',
    description='A lightweight wrapper around the slack web API.',
    entry_points={
        'console_scripts': [
            'scmd=scmd:main',
            'sls=sls:main',
        ],
    },
    keywords=['slack', 'cmd', 'api'],
)

