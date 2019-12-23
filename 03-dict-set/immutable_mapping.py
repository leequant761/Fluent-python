from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy # mappingproxy({1: 'A'})

d_proxy[1] # 'A'
d_proxy[2] = 'B' # Error : not support item assignment

d[2] = 'B'
d_proxy[2] # 'B'


from dis import dis
dis('set([1])')