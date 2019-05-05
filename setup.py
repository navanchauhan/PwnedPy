import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="PwnedPy",
	version="1.0.2019.05",
	author="Navan Chauhan",
	author_email="navanchauhan@gmail.com",
	description="Python Wrapper for Have I Been Pwned API",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/navanchauhan/PwnedPy",
	packages=setuptools.find_packages(),
	install_requires = [
		"requests",
		"json"
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
