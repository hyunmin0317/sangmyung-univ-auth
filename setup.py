import setuptools
from setuptools import setup
from sangmyung_univ_auth import __VERSION__, __AUTHOR__

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sangmyung-univ-auth',
    version=__VERSION__,
    author=__AUTHOR__,
    author_email='choihm9903@naver.com',
    description='Sangmyung University Students Account Authentication.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hyunmin0317/sangmyung-univ-auth',
    license='MIT',
    keywords='sangmyung univ auth',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'bs4'],
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
