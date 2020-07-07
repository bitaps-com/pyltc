import errno
import os.path
from setuptools import setup, find_packages, Extension

from distutils.command.build_ext import build_ext as _build_ext

class build_ext(_build_ext):
    def run(self):
        if self.distribution.has_c_libraries():
            build_clib = self.get_finalized_command("build_clib")
            self.include_dirs.append(
                os.path.join(build_clib.build_clib, "include"),
            )
            self.include_dirs.extend(build_clib.build_flags['include_dirs'])

            self.library_dirs.append(
                os.path.join(build_clib.build_clib, "lib"),
            )
            self.library_dirs.extend(build_clib.build_flags['library_dirs'])

            self.define = build_clib.build_flags['define']

        return _build_ext.run(self)



setup(name='pyltc',
      version='2.0.1',
      description='Python Litecoin library',
      keywords='bitcoin',
      url='https://github.com/bitaps-com/pyltc',
      author='Alexsei Karpov',
      author_email='admin@bitaps.com',
      license='GPL-3.0',
      install_requires=['pybtc'],
      include_package_data=True,
      package_data={
          'pyltc': ['bip39_word_list/*.txt', 'test/*.txt'],
      },

      cmdclass={ 'build_ext': build_ext, },
      ext_modules=[Extension("_scrypt",
                             ["pyltc/_scrypt/_scrypt.c", "pyltc/_scrypt/_scryptmodule.c"],
                             include_dirs=["pyltc/_scrypt/"])],
      packages=find_packages(),
      test_suite='tests',
      zip_safe=False)
