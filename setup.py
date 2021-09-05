# -*- coding: UTF-8 -*-
import sys
import os
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('__pycache__'):
        shutil.rmtree('__pycache__')
    if os.path.isdir('fly_online.egg-info'):
        shutil.rmtree('fly_online.egg-info')

setup(
    name='fly_online',
    version='0.0.6',
    author='QiangZiBro',
    author_email='qiangzibro@gmail.com',
    url="https://github.com/QiangZiBro/flyOnline",
    description=u'Never get offline in NBU',
    packages=['fly_online'],
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=['selenium', 'geckodriver_autoinstaller'],
    entry_points={
        'console_scripts': [
            'fly=fly_online:fly',
        ]
    }
)
