from ctypes import *

work = CDLL("pydll/*.dll")

print(work)

work.outloaded()

out = work.outadd(5,999)
print(out)
