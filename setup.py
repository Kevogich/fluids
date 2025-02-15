# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Manufacturing',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: BSD',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'Topic :: Scientific/Engineering :: Chemistry',
    'Topic :: Scientific/Engineering :: Physics',
]



from distutils.core import setup
setup(
  name = 'fluids',
  packages = ['fluids'],
  license='MIT',
  version = '0.1.75',
  download_url = 'https://github.com/CalebBell/fluids/tarball/0.1.75',
  description = 'Fluid dynamics component of Chemical Engineering Design Library (ChEDL)',
  long_description=open('README.rst').read(),
  install_requires = ["numpy>=1.5.0", "scipy>=0.9.0"],
  extras_require = {
      'Coverage documentation':  ['wsgiref>=0.1.2', 'coverage>=4.0.3', 'pint']
  },
  author = 'Caleb Bell',
  author_email = 'Caleb.Andrew.Bell@gmail.com',
  platforms=['Windows', 'Linux', 'Mac OS', 'Unix'],
  url = 'https://github.com/CalebBell/fluids',
  keywords = 'fluid dynamics atmosphere pipe fluids compressible fluid dynamics chemical engineering mechanical engineering valve open channel tank friction pressure drop two phase pump drag reynolds sedimentation engineering pipeline process simulation particle size distribution',
  classifiers = classifiers,
  package_data={'fluids': ['data/*', 'nrlmsise00/*', 'optional/*', 'numerics/*', 'constants/*']},
)

