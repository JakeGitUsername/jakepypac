from setuptools import setup, find_packages

setup(
    name='jakepypac',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon jake python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/JakeGitUsername/jakepypac.git',
    author='<Jake Ruele>',
    author_email='<rjruele@gmail.com>'
)
