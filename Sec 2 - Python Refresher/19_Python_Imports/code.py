import sys
print(sys.path)

from module import divide

import module

print(sys.modules)
print(divide(10,2))