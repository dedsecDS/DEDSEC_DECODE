from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dedsec-decode",
    version="1.0.0",
    packages=find_packages(include=['dedsec_decoder', 'dedsec_decoder.*']),
    python_requires=">=3.6",
    
    install_requires=[
        "pyfiglet>=0.8.post1",
        "colorama>=0.4.6",
        "user-agents>=2.2.0"
    ],
    
    entry_points={
        'console_scripts': [
            'DS_DECODE=dedsec_decoder.cli:main',
        ],
    },
    
    author="DedSec",
    author_email="DEDSECVIP@proton.me",
    description="DedSec Binary Encoding/Decoding Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dedsecDS/dedsec-decoder",
    project_urls={
        "Bug Reports": "https://github.com/dedsecDS/dedsec-decoder/issues",
        "Source": "https://github.com/dedsecDS/dedsec-decoder",
    },
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    
    keywords="dedsec, binary, encoder, decoder, security, Famous-Tech",
    
    package_data={
        "dedsec_decoder": ["LICENSE"],
    },
    
    zip_safe=False,
)
