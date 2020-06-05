import os
from setuptools import setup

with open('README', 'r') as fh:
    long_description = fh.read()

setup(
    name='dj-migration-test',
    packages=['dj_migration_test'],
    version=os.environ.get('TAG', 'v0.2.1'),
    license='MIT',
    description='Django migration test module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Philipp Zettl',
    author_email='philipp.zettl@godesteem.de',
    url='https://github.com/philsupertramp/dj-migration-test',
    download_url=f'https://github.com/philsupertramp/dj-migration-test/archive/{os.environ.get("TAG", "v0.2.1")}.tar.gz',
    keywords=['Django', 'Testing', 'Database'],
    install_requires=[
        'django>=2.2.13'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        # '3 - Alpha', '4 - Beta' or '5 - Production/Stable'
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Bug Tracking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
)
