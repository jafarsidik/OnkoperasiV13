from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in onkoperasiv13/__init__.py
from onkoperasiv13 import __version__ as version

setup(
	name="onkoperasiv13",
	version=version,
	description="Aplikasi Onkoperasi Version 13",
	author="Muhamad Jafar Sidik",
	author_email="official.jafarsidik@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
