from patternmatching import *
from algo1 import *


s1 = String('ab*bacb*a')
s2 = String('cabccbacbacab')
c = '*'

print(isPatternContained(s1,s2,c))