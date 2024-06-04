from setuptools import setup, find_packages

setup(
    name='Ghaflankoo_shamsi',
    version='1.0.0',
    packages=find_packages(),
    description="Jalali datetime convert for python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="mehdi ghaffari moghaddam",
    author_email="mehdi.ghaffari.moghaddam@gmail.com",
    url="https://github.com/mehdigh125/Ghaflanko_shamsi.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
    ],
    
    python_requires='>=3.6',
)
