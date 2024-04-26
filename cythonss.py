from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("cython_1_0.pyx"))
setup(ext_modules = cythonize("cython_2_0.pyx"))
setup(ext_modules = cythonize("cython_3_0.pyx"))
setup(ext_modules = cythonize("cython_4_0.pyx"))