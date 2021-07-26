#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup

DESCRIPTION = 'webui for youtube-dl'
LONG_DESCRIPTION = 'Another webui for youtube-dl, powered by youtube-dl'

setup (
        name='youtube_dl_webui',
        version='0.0.1',
        packages=['youtube_dl_webui'],
        license='GPL-2.0',
        author='d0u9, yuanyingfeiyu',
        author_email='d0u9.su@outlook.com',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        include_package_data=True,
        package_data={'': ['logging.json','schema.sql','static/**/*','static/font-awesome/*/**.*','templates/*']},
        zip_safe=False,
        install_requires=[
            'Flask>=0.2',
            'youtube-dl',
        ],
        entry_points={
            'console_scripts': [
                'youtube-dl-webui = youtube_dl_webui:main'
            ]
        },
)
