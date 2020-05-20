from setuptools import find_packages, setup

install_requires = [
    "aiohttp~=3.4",
    "arrow~=0.14",
    "pip-tools==5.1.2",
    "pydantic~=1.3",
]

setup(
    name="dependatest",
    version="0.0.1",
    author="Dependa Test",
    author_email="dependa.test@example.com",
    description="dependatest",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    python_requires=">=3.7",
)
