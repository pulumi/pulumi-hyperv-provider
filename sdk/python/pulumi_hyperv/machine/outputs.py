# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'HardDriveInput',
]

@pulumi.output_type
class HardDriveInput(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "controllerLocation":
            suggest = "controller_location"
        elif key == "controllerNumber":
            suggest = "controller_number"
        elif key == "controllerType":
            suggest = "controller_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HardDriveInput. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HardDriveInput.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HardDriveInput.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 controller_location: builtins.int,
                 controller_number: builtins.int,
                 controller_type: builtins.str,
                 path: builtins.str):
        pulumi.set(__self__, "controller_location", controller_location)
        pulumi.set(__self__, "controller_number", controller_number)
        pulumi.set(__self__, "controller_type", controller_type)
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="controllerLocation")
    def controller_location(self) -> builtins.int:
        return pulumi.get(self, "controller_location")

    @property
    @pulumi.getter(name="controllerNumber")
    def controller_number(self) -> builtins.int:
        return pulumi.get(self, "controller_number")

    @property
    @pulumi.getter(name="controllerType")
    def controller_type(self) -> builtins.str:
        return pulumi.get(self, "controller_type")

    @property
    @pulumi.getter
    def path(self) -> builtins.str:
        return pulumi.get(self, "path")


