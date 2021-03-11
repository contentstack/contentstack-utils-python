import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

setup(
    name='contentstack_utils',
    packages=find_packages(include=['contentstack']),
    description="contentstack_utils is a Utility package for Contentstack headless CMS with an API-first approach.",
    author='contentstack',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/contentstack/contentstack-utils-python",
    version='0.0.1',
    license='MIT',
    install_requires=[ 
        pip~=21.0.1
        setuptools~=47.1.0
        lxml~=4.6.2
        pylint
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    python_requires='>=3.6',
)
