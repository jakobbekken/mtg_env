from setuptools import setup, find_packages

setup(
    name="mtg_env",
    version="0.1.0",
    description="A Magic: The Gathering game environment with rules enforcement.",
    author="Jakob Moen Bekken",
    author_email="post@jokko.no",
    url="https://github.com/jakobbekken/mtg_env",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Private :: Do Not Upload",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "Topic :: Games/Etertainment :: Simulation",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operation System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.12"
)
