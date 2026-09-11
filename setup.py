from setuptools import setup, find_packages

setup(
    name="unifiedkappa",
    version="0.1.0",
    description="Unified Thermal Conductivity Toolkit",
    packages=find_packages(),
    install_requires=[
        "ase",
    ],
    entry_points={
        "console_scripts": [
            "unifiedkappa=unifiedkappa.script_kappa_deg:main",
        ],
    },
    python_requires=">=3.7",
)