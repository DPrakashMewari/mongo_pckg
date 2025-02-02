from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "mongodb_pkg"
PKG_NAME = "dbauto"
AUTHOR_USER_NAME = "prakashM"
AUTHOR_EMAIL = "prakash.mewari@yahoo.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Correct keyword here
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    # packages=find_packages(where="src"),  # Automatically find packages in the src folder
    install_requires=[  # External dependencies should go here
        'pymongo',
        'pymongo[srv]',
        'dnspython',
        'pandas',
        'numpy',
        'ensure',
        'pytest',
    ],
    python_requires='>=3.6',  # Specify Python version requirements
)
