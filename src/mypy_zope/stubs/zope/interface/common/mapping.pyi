from zope.interface import Interface

class IItemMapping(Interface):
    def __getitem__(key): ...

class IReadMapping(IItemMapping):
    def get(key, default=None): ...
    def __contains__(key): ...

class IWriteMapping(Interface):
    def __delitem__(key): ...
    def __setitem__(key, value): ...

class IEnumerableMapping(IReadMapping):
    def keys(): ...
    def __iter__(): ...
    def values(): ...
    def items(): ...
    def __len__(): ...

class IMapping(IWriteMapping, IEnumerableMapping):
    ...

class IIterableMapping(IEnumerableMapping):
    def iterkeys(): ...
    def itervalues(): ...
    def iteritems(): ...

class IClonableMapping(Interface):
    def copy(): ...

class IExtendedReadMapping(IIterableMapping):
    def has_key(key): ...

class IExtendedWriteMapping(IWriteMapping):
    def clear(): ...
    def update(d): ...
    def setdefault(key, default=None): ...
    def pop(k, *args): ...
    def popitem(): ...

class IFullMapping(
    IExtendedReadMapping, IExtendedWriteMapping, IClonableMapping, IMapping):
    ...