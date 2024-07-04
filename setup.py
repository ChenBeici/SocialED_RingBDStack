from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='SocialED',
    version='0.1.0',
    packages=find_packages(),
    author='beici',
    author_email='SY2339225@buaa.edu.cn',
    description='A Python Library for Social Event Detection',
    install_requires=requirements,
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kobebryantlakers/socialED',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)