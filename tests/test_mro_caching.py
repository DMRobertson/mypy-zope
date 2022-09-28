from mypy import options, build
from mypy.modulefinder import BuildSource


SOURCE_CODE = """
from twisted.internet import protocol

class Foo(protocol.Protocol):
    pass
"""

opts = options.Options()
opts.cache_dir = '.mypy_cache_dmr'
opts.show_traceback = True
opts.namespace_packages = True
opts.plugins = ['mypy_zope:plugin']
# Config file is needed to load plugins, it doesn't not exist and is not
# supposed to.
opts.config_file = '    not_existing_config.ini'

source = BuildSource(None,
                     module=None,
                     text=SOURCE_CODE,
                     base_dir=None)
res1 = build.build(
    sources=[source],
    options=opts)

print(res1.errors)

res2 = build.build(
    sources=[source],
    options=opts)

print(res2.errors)