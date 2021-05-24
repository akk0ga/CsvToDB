import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Csv-To-DB",
    version="0.0.4",
    author="akk0ga",
    author_email="ttn.glock@orange.fr",
    description="Make it easier to build database/table/seeders for DBMS or web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/akk0ga/csv_parser",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=setuptools.find_packages(),
    keywords=['csv', 'db', 'database', 'sql', 'framework', 'mysql'],
    python_requires=">=3.6",
)
