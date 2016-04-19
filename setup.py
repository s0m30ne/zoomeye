import codecs
import os
import sys
 
try:
    from setuptools import setup
except:
    from distutils.core import setup
 
def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()
 
 
 
NAME = "zoomeye"
 
PACKAGES = ["zoomeye",]
 
DESCRIPTION = "zoomeye sdk for you to explore the web space."

LONG_DESCRIPTION = read("README.txt")

KEYWORDS = "zoomeye sdk"
 
AUTHOR = "s0m30ne"
 
AUTHOR_EMAIL = "s0m30ne@163.com"
 
URL = ""
 
VERSION = "1.0"
 
LICENSE = "MIT"
 
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Security',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)