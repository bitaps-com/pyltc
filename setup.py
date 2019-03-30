#!/usr/bin/python3
# coding: utf-8

from setuptools import setup, find_packages, Extension


setup(name='pyltc',
      version='2.0.0',
      description='Python Litecoin library',
      keywords='bitcoin',
      url='https://github.com/bitaps-com/pyltc',
      author='Alexsei Karpov',
      author_email='admin@bitaps.com',
      license='GPL-3.0',
      packages=find_packages(),
      install_requires=['pybtc'],
      include_package_data=True,
      package_data={
          'pyltc': ['bip39_word_list/*.txt', 'test/*.txt'],
      },
      test_suite='tests',
      ext_modules=[Extension("ltc_scrypt",
                             ["pyltc/scrypt/scrypt.c", "pyltc/scrypt/scryptmodule.c"],
                             include_dirs=["pyltc/scrypt"])],
      zip_safe=False)
