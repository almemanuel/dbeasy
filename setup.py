import re
from setuptools import setup

with open('dbeasy/__init__.py', 'r', encoding="utf-8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md', 'r', encoding="utf-8") as f:
    readme = f.read()

setup(
    name='dbeasy',
    version=version,
    packages=['dbeasy'],
    url='https://github.com/almemanuel/dbeasy',
    project_urls={
        'Issue tracker': 'https://github.com/almemanuel/dbeasy/issues'
    },
    license='MIT',
    author='almemanuel',
    description='Simple database interface.',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'typing',
        'datetime',
        'schedule',
        'tabulate',
        'pymssql'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
