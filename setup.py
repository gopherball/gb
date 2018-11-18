from setuptools import setup


setup(
    name="gb",
    version="1.0.0",
    description="A Python gopher server.",
    url="https://github.com/supakeen/gb",
    author="supakeen",
    author_email="cmdr@supakeen.com",
    packages=[],
    setup_requires=["pytest-runner", "pytest-cov"],
    install_requires=["tornado", "click", "python-magic"],
    entry_points={"console_scripts": ["gb=gb.command:main"]},
    tests_require=["pytest", "pytest-cov"],
    extras_require={"dev": ["pre-commit", "flake8", "black", "nose"]},
)
