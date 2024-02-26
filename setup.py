from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='akshay-helloworld',
	version='0.0.2',
	author = "Akshay Dongare",
	description='Python package to print Hello World!',
	long_description = read('README.md'),
	long_description_content_type = "text/markdown",
	license_files = ('LICENSE.txt',),
	py_modules=["akshay_helloworld"],
	package_dir={'': 'src'},
	classifiers=[
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.9",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
	],
)