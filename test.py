
import unittest

import pyltc.test

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(pyltc.test)

runner = unittest.TextTestRunner(verbosity=1)
runner.run(suites)