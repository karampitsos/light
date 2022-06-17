from setuptools import setup


with open("README.md", 'r') as file:
    readme = file.read()

setup(
    name='phos',
    version='0.0.1',
    description='This is a raw8 parser',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Nikolaos Karampitsos',
    author_email='nikolaos.karampitsos@gmail.com',
    url='https://github.com/karampitsos/light',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT License',
    packages=['phos'],
    python_requires=">=3.7",
    package_dir={'phos': 'phos'},
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    }
)

#for distribution
#python3 -m pip install build
#python3 -m build
#python3 -m pip install twine
#for testing
#python3 -m twine upload --repository testpypi dist/*
#for production
#python3 -m twine upload dist/*
#pip install -i https://test.pypi.org/simple/ phos==0.0.1