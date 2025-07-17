from setuptools import setup
from Cython.Build import cythonize
setup(
    name="Ainsley Tool",
    ext_modules=cythonize("ainsley.py"),
    zip_safe=False,
)
