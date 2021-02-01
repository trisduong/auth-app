import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="authapp123",
    version="0.1.1",
    author="Tris",
    author_email="duongvantri1998@gmail.com",
    description="Authorization basic app for flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trisduong/authapp123",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'bs4>=0.0.1',
        'certifi>=2020.12.5',
        'chardet>=4.0.0',
        'click>=7.1.2',
        'Flask>=1.1.2',
        'html5lib>=1.1',
        'idna>=2.10',
        'itsdangerous>=1.1.0',
        'Jinja2>=2.11.3',
        'MarkupSafe>=1.1.1',
        'requests>=2.25.1',
        'six>=1.15.0',
        'soupsieve>=2.1',
        'urllib3>=1.26.3',
        'webencodings>=0.5.1',
        'Werkzeug>=1.0.1',
    ]
)
