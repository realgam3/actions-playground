#!/usr/bin/env python3

from os import path
from setuptools import setup, find_packages

__folder__ = path.abspath(path.dirname(__file__))

setup(
    name="actions-playground",
    version="0.1.4",
    description="actions-playground",
    long_description="actions-playground",
    long_description_content_type='text/markdown',
    author="Tomer Zait (realgam3)",
    author_email="realgam3@gmail.com",
    packages=find_packages(exclude=['examples', 'tests']),
    entry_points={
        "console_scripts": [
            'actions-playground = actions_playground:main',
        ]
    },
    python_requires=">=3.7",
    install_requires=[],
    license="Apache 2.0",
    platforms='any',
    url="https://github.com/realgam3/actions-playground",
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    project_urls={
        'Source': "https://github.com/realgam3/actions-playground",
    },
)
