import shutil
from pprint import pprint

from mypy import options, build
from mypy.fscache import FileSystemCache
from mypy.modulefinder import BuildSource

SOURCE_CODE = """
from twisted.internet import protocol

class Foo(protocol.Protocol):
    pass
"""

opts = options.Options()
opts.show_traceback = True
opts.namespace_packages = True
opts.cache_dir = ".mypy_cache_dmr"
opts.mypy_path = ["tests/playground/site-packages"]
opts.ignore_missing_imports = True
opts.ignore_missing_imports_per_module = True
opts.plugins = ['mypy_zope:plugin']
# Config file is needed to load plugins, it doesn't not exist and is not
# supposed to.
opts.config_file = '    not_existing_config.ini'

shutil.rmtree(".mypy_cache_dmr/3.10/twisted", ignore_errors=True)

source = BuildSource(None,
                     module=None,
                     text=SOURCE_CODE,
                     base_dir=None)
cache = FileSystemCache()
results = []
for i in range(2):
    result = build.build(
        sources=[source],
        options=opts,
    )

    pprint(result.errors)
    results.append(result)

assert not results[0].errors, results[1].errors
assert not results[1].errors, results[1].errors
