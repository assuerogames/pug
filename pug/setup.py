from setuptools import setup, find_packages

setup(
    name='pug',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    author='Dário Assuero',
    author_email='assuerodario5@gmail.com',
    description='Uma biblioteca Python chamada Pug',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/assuerogames/pug',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
