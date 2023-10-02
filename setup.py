'''
endpoints
Copyright (C) 2023  Ramon Moraes

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
'''


from setuptools import setup, find_packages
from endpoints import (
        __version__,
        __author__,
        __author_email__,
        __license__,
        __app_name__,
        __description__,
    )


with open('README.md') as f:
    __long_description__ = f.read()


setup(
    name=__app_name__,
    version=__version__,
    url='https://gitlab.com/velvetkeyboad/py-endpoints',
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    description=__description__,
    long_description=__long_description__,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.0.0',
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
