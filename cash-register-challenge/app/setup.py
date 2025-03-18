from setuptools import find_packages, setup


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(name='cash-register-app',
      version="1.0.1",
      description="Checkout calculator with discounts capabilities",
      license="unlicense",
      author="patepelo",
      author_email="developing.anton@gmail.com",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",)
