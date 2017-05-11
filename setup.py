from numpy.distutils.core import setup
from numpy.distutils.extension import Extension

extension = Extension("gcvspline._gcvspl", ["gcvspline/gcvspl.f"])

setup(name='gcvspline',
      version='0.2',
      description='A wrapper for gcvspl.f, a FORTRAN package for generalized, cross-validatory spline smoothing and differentiation.',
      url='http://github.com/storborg/funniest',
      author='Charles Le Losq',
      author_email='charles.lelosq@anu.edu.au',
      license='GNU-GPLv3',
      packages=['gcvspline', 'gcvspline.tests'],
      ext_modules=[extension],
      zip_safe=False)
