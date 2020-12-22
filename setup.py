import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="amazon_affiliate_url",
    version="0.0.7",
    author="Kristof",
    description="amazon_affiliate_url",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/amazon_affiliate_url",
    packages=setuptools.find_packages(),
    install_requires=["bitlyshortener"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)