# -*- coding: utf-8 -*-

from numpy import *

import trees

myDat, labels= trees.createDataSet()
assert isinstance(myDat, object)
trees.chooseBestFeatureToSplit(myDat)
print myDat

# s = '中文'
# s.decode('utf-8').encode('gb18030')
