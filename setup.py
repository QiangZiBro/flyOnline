# -*- coding: UTF-8 -*-
from setuptools import setup

setup(
    name='fly_online',
    version='0.0.5',
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
