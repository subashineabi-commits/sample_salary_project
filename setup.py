from setuptools import setup, find_packages

setup(
    name="DEMO",   # Your project/package name
    version="0.1.0",               # Initial version
    description="A project for analyzing student performance data",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),      # Automatically find all packages in your project
    install_requires=[             # Dependencies
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib"
    ],
    python_requires=">=3.8",       # Minimum Python version
)
