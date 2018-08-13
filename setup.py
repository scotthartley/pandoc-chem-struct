from setuptools import setup


def readme():
    with open("README.rst") as file:
        return file.read()


setup(name="pandoc-chem-struct",
      version=1.0,
      description=("Interpret chemical formulas in pandoc"),
      long_description=readme(),
      author="Scott Hartley",
      author_email="scott.hartley@miamioh.edu",
      url="https://hartleygroup.org",
      license="MIT",
      scripts=["pandoc-chem-struct"],
      packages=["pandoc_chem_struct"],
      install_requires=["pandocfilters"],
      python_requires=">=3",
      )
