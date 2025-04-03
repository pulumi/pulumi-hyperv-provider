# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_hyperv.config as __config
    config = __config
    import pulumi_hyperv.vm as __vm
    vm = __vm
else:
    config = _utilities.lazy_import('pulumi_hyperv.config')
    vm = _utilities.lazy_import('pulumi_hyperv.vm')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "hyperv",
  "mod": "vm",
  "fqn": "pulumi_hyperv.vm",
  "classes": {
   "hyperv:vm:Vm": "Vm"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "hyperv",
  "token": "pulumi:providers:hyperv",
  "fqn": "pulumi_hyperv",
  "class": "Provider"
 }
]
"""
)
