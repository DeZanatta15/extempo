from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "modules/cython_1_0.pyx",
        "modules/cython_2_0.pyx",
        "modules/cython_3_0.pyx",
        "modules/cython_4_0.pyx"
    ]),
    zip_safe=False
)