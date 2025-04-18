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
from . import outputs
from ...\. import networkadapter as _networkadapter
from ._inputs import *

__all__ = ['MachineArgs', 'Machine']

@pulumi.input_type
class MachineArgs:
    def __init__(__self__, *,
                 auto_start_action: Optional[pulumi.Input[builtins.str]] = None,
                 auto_stop_action: Optional[pulumi.Input[builtins.str]] = None,
                 create: Optional[pulumi.Input[builtins.str]] = None,
                 delete: Optional[pulumi.Input[builtins.str]] = None,
                 dynamic_memory: Optional[pulumi.Input[builtins.bool]] = None,
                 generation: Optional[pulumi.Input[builtins.int]] = None,
                 hard_drives: Optional[pulumi.Input[Sequence[pulumi.Input['HardDriveInputArgs']]]] = None,
                 machine_name: Optional[pulumi.Input[builtins.str]] = None,
                 maximum_memory: Optional[pulumi.Input[builtins.int]] = None,
                 memory_size: Optional[pulumi.Input[builtins.int]] = None,
                 minimum_memory: Optional[pulumi.Input[builtins.int]] = None,
                 network_adapters: Optional[pulumi.Input[Sequence[pulumi.Input['_networkadapter.NetworkAdapterInputsArgs']]]] = None,
                 processor_count: Optional[pulumi.Input[builtins.int]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 update: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Machine resource.
        :param pulumi.Input[builtins.str] auto_start_action: The action to take when the host starts. Valid values are Nothing, StartIfRunning, and Start. Defaults to Nothing.
        :param pulumi.Input[builtins.str] auto_stop_action: The action to take when the host shuts down. Valid values are TurnOff, Save, and ShutDown. Defaults to TurnOff.
        :param pulumi.Input[builtins.str] create: The command to run on create.
        :param pulumi.Input[builtins.str] delete: The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
               and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
               Command resource from previous create or update steps.
        :param pulumi.Input[builtins.bool] dynamic_memory: Whether to enable dynamic memory for the Virtual Machine. Defaults to false.
        :param pulumi.Input[builtins.int] generation: Generation of the Virtual Machine. Defaults to 2.
        :param pulumi.Input[Sequence[pulumi.Input['HardDriveInputArgs']]] hard_drives: Hard drives to attach to the Virtual Machine.
        :param pulumi.Input[builtins.str] machine_name: Name of the Virtual Machine
        :param pulumi.Input[builtins.int] maximum_memory: Maximum amount of memory that can be allocated to the Virtual Machine in MB when using dynamic memory.
        :param pulumi.Input[builtins.int] memory_size: Amount of memory to allocate to the Virtual Machine in MB. Defaults to 1024.
        :param pulumi.Input[builtins.int] minimum_memory: Minimum amount of memory to allocate to the Virtual Machine in MB when using dynamic memory.
        :param pulumi.Input[Sequence[pulumi.Input['_networkadapter.NetworkAdapterInputsArgs']]] network_adapters: Network adapters to attach to the Virtual Machine.
        :param pulumi.Input[builtins.int] processor_count: Number of processors to allocate to the Virtual Machine. Defaults to 1.
        :param pulumi.Input[Sequence[Any]] triggers: Trigger a resource replacement on changes to any of these values. The
               trigger values can be of any type. If a value is different in the current update compared to the
               previous update, the resource will be replaced, i.e., the "create" command will be re-run.
               Please see the resource documentation for examples.
        :param pulumi.Input[builtins.str] update: The command to run on update, if empty, create will 
               run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
               are set to the stdout and stderr properties of the Command resource from previous 
               create or update steps.
        """
        if auto_start_action is not None:
            pulumi.set(__self__, "auto_start_action", auto_start_action)
        if auto_stop_action is not None:
            pulumi.set(__self__, "auto_stop_action", auto_stop_action)
        if create is not None:
            pulumi.set(__self__, "create", create)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if dynamic_memory is not None:
            pulumi.set(__self__, "dynamic_memory", dynamic_memory)
        if generation is not None:
            pulumi.set(__self__, "generation", generation)
        if hard_drives is not None:
            pulumi.set(__self__, "hard_drives", hard_drives)
        if machine_name is not None:
            pulumi.set(__self__, "machine_name", machine_name)
        if maximum_memory is not None:
            pulumi.set(__self__, "maximum_memory", maximum_memory)
        if memory_size is not None:
            pulumi.set(__self__, "memory_size", memory_size)
        if minimum_memory is not None:
            pulumi.set(__self__, "minimum_memory", minimum_memory)
        if network_adapters is not None:
            pulumi.set(__self__, "network_adapters", network_adapters)
        if processor_count is not None:
            pulumi.set(__self__, "processor_count", processor_count)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @property
    @pulumi.getter(name="autoStartAction")
    def auto_start_action(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The action to take when the host starts. Valid values are Nothing, StartIfRunning, and Start. Defaults to Nothing.
        """
        return pulumi.get(self, "auto_start_action")

    @auto_start_action.setter
    def auto_start_action(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "auto_start_action", value)

    @property
    @pulumi.getter(name="autoStopAction")
    def auto_stop_action(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The action to take when the host shuts down. Valid values are TurnOff, Save, and ShutDown. Defaults to TurnOff.
        """
        return pulumi.get(self, "auto_stop_action")

    @auto_stop_action.setter
    def auto_stop_action(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "auto_stop_action", value)

    @property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The command to run on create.
        """
        return pulumi.get(self, "create")

    @create.setter
    def create(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "create", value)

    @property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
        and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
        Command resource from previous create or update steps.
        """
        return pulumi.get(self, "delete")

    @delete.setter
    def delete(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "delete", value)

    @property
    @pulumi.getter(name="dynamicMemory")
    def dynamic_memory(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Whether to enable dynamic memory for the Virtual Machine. Defaults to false.
        """
        return pulumi.get(self, "dynamic_memory")

    @dynamic_memory.setter
    def dynamic_memory(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "dynamic_memory", value)

    @property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Generation of the Virtual Machine. Defaults to 2.
        """
        return pulumi.get(self, "generation")

    @generation.setter
    def generation(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "generation", value)

    @property
    @pulumi.getter(name="hardDrives")
    def hard_drives(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HardDriveInputArgs']]]]:
        """
        Hard drives to attach to the Virtual Machine.
        """
        return pulumi.get(self, "hard_drives")

    @hard_drives.setter
    def hard_drives(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HardDriveInputArgs']]]]):
        pulumi.set(self, "hard_drives", value)

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Name of the Virtual Machine
        """
        return pulumi.get(self, "machine_name")

    @machine_name.setter
    def machine_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "machine_name", value)

    @property
    @pulumi.getter(name="maximumMemory")
    def maximum_memory(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Maximum amount of memory that can be allocated to the Virtual Machine in MB when using dynamic memory.
        """
        return pulumi.get(self, "maximum_memory")

    @maximum_memory.setter
    def maximum_memory(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "maximum_memory", value)

    @property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Amount of memory to allocate to the Virtual Machine in MB. Defaults to 1024.
        """
        return pulumi.get(self, "memory_size")

    @memory_size.setter
    def memory_size(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "memory_size", value)

    @property
    @pulumi.getter(name="minimumMemory")
    def minimum_memory(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Minimum amount of memory to allocate to the Virtual Machine in MB when using dynamic memory.
        """
        return pulumi.get(self, "minimum_memory")

    @minimum_memory.setter
    def minimum_memory(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "minimum_memory", value)

    @property
    @pulumi.getter(name="networkAdapters")
    def network_adapters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_networkadapter.NetworkAdapterInputsArgs']]]]:
        """
        Network adapters to attach to the Virtual Machine.
        """
        return pulumi.get(self, "network_adapters")

    @network_adapters.setter
    def network_adapters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_networkadapter.NetworkAdapterInputsArgs']]]]):
        pulumi.set(self, "network_adapters", value)

    @property
    @pulumi.getter(name="processorCount")
    def processor_count(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Number of processors to allocate to the Virtual Machine. Defaults to 1.
        """
        return pulumi.get(self, "processor_count")

    @processor_count.setter
    def processor_count(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "processor_count", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        """
        Trigger a resource replacement on changes to any of these values. The
        trigger values can be of any type. If a value is different in the current update compared to the
        previous update, the resource will be replaced, i.e., the "create" command will be re-run.
        Please see the resource documentation for examples.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "triggers", value)

    @property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The command to run on update, if empty, create will 
        run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
        are set to the stdout and stderr properties of the Command resource from previous 
        create or update steps.
        """
        return pulumi.get(self, "update")

    @update.setter
    def update(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "update", value)


class Machine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_start_action: Optional[pulumi.Input[builtins.str]] = None,
                 auto_stop_action: Optional[pulumi.Input[builtins.str]] = None,
                 create: Optional[pulumi.Input[builtins.str]] = None,
                 delete: Optional[pulumi.Input[builtins.str]] = None,
                 dynamic_memory: Optional[pulumi.Input[builtins.bool]] = None,
                 generation: Optional[pulumi.Input[builtins.int]] = None,
                 hard_drives: Optional[pulumi.Input[Sequence[pulumi.Input[Union['HardDriveInputArgs', 'HardDriveInputArgsDict']]]]] = None,
                 machine_name: Optional[pulumi.Input[builtins.str]] = None,
                 maximum_memory: Optional[pulumi.Input[builtins.int]] = None,
                 memory_size: Optional[pulumi.Input[builtins.int]] = None,
                 minimum_memory: Optional[pulumi.Input[builtins.int]] = None,
                 network_adapters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_networkadapter.NetworkAdapterInputsArgs', '_networkadapter.NetworkAdapterInputsArgsDict']]]]] = None,
                 processor_count: Optional[pulumi.Input[builtins.int]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 update: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        # Hyper-V Machine Resource

        ## Overview

        The Machine resource in the Pulumi Hyper-V provider allows you to create, manage, and delete virtual machines on a Hyper-V host. This resource interacts with the Virtual Machine Management Service (VMMS) to perform virtual machine operations.

        ## Features

        - Create and delete Hyper-V virtual machines
        - Configure VM hardware properties including:
          - Memory allocation (static or dynamic with min/max)
          - Processor count
          - VM generation (Gen 1 or Gen 2)
          - Auto start/stop actions
        - Attach hard drives with custom controller configuration
        - Configure network adapters with virtual switch connections
        - Unique VM identification with automatic ID generation

        ## Implementation Details

        ### Resource Structure

        The Machine resource implementation consists of multiple files:
        - `machine.go` - Core resource type definition, input/output models, and annotations
        - `machineController.go` - Implementation of CRUD operations
        - `machineOutputs.go` - Output-specific methods

        ### Virtual Machine Creation

        The `Create` method performs the following steps:

        1. **Initialize Connection**: Establishes a connection to the Hyper-V host using WMI
        2. **Configure VM Settings**:
           - Sets the virtual machine generation (defaults to Generation 2)
           - Configures memory settings (defaults to 1024 MB)
           - Sets dynamic memory with min/max values if requested
           - Sets processor count (defaults to 1 vCPU)
           - Configures auto start/stop actions
        3. **Create VM**: Calls the Hyper-V API to create a new virtual machine with the specified settings
        4. **Attach Hard Drives**: Attaches any specified hard drives to the VM
        5. **Configure Network Adapters**: Adds any specified network adapters to the VM

        ### Virtual Machine Read

        The `Read` method retrieves the current state of a virtual machine by:
        1. Connecting to the Hyper-V host
        2. Getting the VM by name
        3. Retrieving VM properties including:
           - VM ID
           - Memory settings (including dynamic memory configuration)
           - Processor configuration
           - Generation
           - Auto start/stop actions

        ### Virtual Machine Update

        The `Update` method currently provides a minimal implementation that preserves the VM's state while updating its metadata.

        ### Virtual Machine Delete

        The `Delete` method:
        1. Connects to the Hyper-V host
        2. Gets the virtual machine by name
        3. Starts the VM (to ensure it's in a state that can be properly deleted)
        4. Gracefully stops the VM
        5. Deletes the virtual machine

        ## Available Properties

        | Property | Type | Description | Default |
        |----------|------|-------------|---------|
        | `machineName` | string | Name of the Virtual Machine | (required) |
        | `generation` | int | Generation of the Virtual Machine (1 or 2) | 2 |
        | `processorCount` | int | Number of processors to allocate | 1 |
        | `memorySize` | int | Memory size in MB | 1024 |
        | `dynamicMemory` | bool | Enable dynamic memory for the VM | false |
        | `minimumMemory` | int | Minimum memory in MB when using dynamic memory | - |
        | `maximumMemory` | int | Maximum memory in MB when using dynamic memory | - |
        | `autoStartAction` | string | Action on host start (Nothing, StartIfRunning, Start) | Nothing |
        | `autoStopAction` | string | Action on host shutdown (TurnOff, Save, ShutDown) | TurnOff |
        | `networkAdapters` | array | Network adapters to attach to the VM | [] |
        | `hardDrives` | array | Hard drives to attach to the VM | [] |
        | `triggers` | array | Values that trigger resource replacement when changed | (optional) |

        ### Network Adapter Properties

        | Property | Type | Description | Default |
        |----------|------|-------------|---------|
        | `name` | string | Name of the network adapter | "Network Adapter" |
        | `switchName` | string | Name of the virtual switch to connect to | (required) |

        ### Hard Drive Properties

        | Property | Type | Description | Default |
        |----------|------|-------------|---------|
        | `path` | string | Path to the VHD/VHDX file | (required) |
        | `controllerType` | string | Type of controller (IDE or SCSI) | SCSI |
        | `controllerNumber` | int | Controller number | 0 |
        | `controllerLocation` | int | Controller location | 0 |

        ## Usage Examples

        ## Related Documentation

        - [Microsoft Hyper-V Documentation](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server)
        - [Pulumi Hyper-V Provider Documentation](https://www.pulumi.com/registry/packages/hyperv/)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] auto_start_action: The action to take when the host starts. Valid values are Nothing, StartIfRunning, and Start. Defaults to Nothing.
        :param pulumi.Input[builtins.str] auto_stop_action: The action to take when the host shuts down. Valid values are TurnOff, Save, and ShutDown. Defaults to TurnOff.
        :param pulumi.Input[builtins.str] create: The command to run on create.
        :param pulumi.Input[builtins.str] delete: The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
               and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
               Command resource from previous create or update steps.
        :param pulumi.Input[builtins.bool] dynamic_memory: Whether to enable dynamic memory for the Virtual Machine. Defaults to false.
        :param pulumi.Input[builtins.int] generation: Generation of the Virtual Machine. Defaults to 2.
        :param pulumi.Input[Sequence[pulumi.Input[Union['HardDriveInputArgs', 'HardDriveInputArgsDict']]]] hard_drives: Hard drives to attach to the Virtual Machine.
        :param pulumi.Input[builtins.str] machine_name: Name of the Virtual Machine
        :param pulumi.Input[builtins.int] maximum_memory: Maximum amount of memory that can be allocated to the Virtual Machine in MB when using dynamic memory.
        :param pulumi.Input[builtins.int] memory_size: Amount of memory to allocate to the Virtual Machine in MB. Defaults to 1024.
        :param pulumi.Input[builtins.int] minimum_memory: Minimum amount of memory to allocate to the Virtual Machine in MB when using dynamic memory.
        :param pulumi.Input[Sequence[pulumi.Input[Union['_networkadapter.NetworkAdapterInputsArgs', '_networkadapter.NetworkAdapterInputsArgsDict']]]] network_adapters: Network adapters to attach to the Virtual Machine.
        :param pulumi.Input[builtins.int] processor_count: Number of processors to allocate to the Virtual Machine. Defaults to 1.
        :param pulumi.Input[Sequence[Any]] triggers: Trigger a resource replacement on changes to any of these values. The
               trigger values can be of any type. If a value is different in the current update compared to the
               previous update, the resource will be replaced, i.e., the "create" command will be re-run.
               Please see the resource documentation for examples.
        :param pulumi.Input[builtins.str] update: The command to run on update, if empty, create will 
               run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
               are set to the stdout and stderr properties of the Command resource from previous 
               create or update steps.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MachineArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        # Hyper-V Machine Resource

        ## Overview

        The Machine resource in the Pulumi Hyper-V provider allows you to create, manage, and delete virtual machines on a Hyper-V host. This resource interacts with the Virtual Machine Management Service (VMMS) to perform virtual machine operations.

        ## Features

        - Create and delete Hyper-V virtual machines
        - Configure VM hardware properties including:
          - Memory allocation (static or dynamic with min/max)
          - Processor count
          - VM generation (Gen 1 or Gen 2)
          - Auto start/stop actions
        - Attach hard drives with custom controller configuration
        - Configure network adapters with virtual switch connections
        - Unique VM identification with automatic ID generation

        ## Implementation Details

        ### Resource Structure

        The Machine resource implementation consists of multiple files:
        - `machine.go` - Core resource type definition, input/output models, and annotations
        - `machineController.go` - Implementation of CRUD operations
        - `machineOutputs.go` - Output-specific methods

        ### Virtual Machine Creation

        The `Create` method performs the following steps:

        1. **Initialize Connection**: Establishes a connection to the Hyper-V host using WMI
        2. **Configure VM Settings**:
           - Sets the virtual machine generation (defaults to Generation 2)
           - Configures memory settings (defaults to 1024 MB)
           - Sets dynamic memory with min/max values if requested
           - Sets processor count (defaults to 1 vCPU)
           - Configures auto start/stop actions
        3. **Create VM**: Calls the Hyper-V API to create a new virtual machine with the specified settings
        4. **Attach Hard Drives**: Attaches any specified hard drives to the VM
        5. **Configure Network Adapters**: Adds any specified network adapters to the VM

        ### Virtual Machine Read

        The `Read` method retrieves the current state of a virtual machine by:
        1. Connecting to the Hyper-V host
        2. Getting the VM by name
        3. Retrieving VM properties including:
           - VM ID
           - Memory settings (including dynamic memory configuration)
           - Processor configuration
           - Generation
           - Auto start/stop actions

        ### Virtual Machine Update

        The `Update` method currently provides a minimal implementation that preserves the VM's state while updating its metadata.

        ### Virtual Machine Delete

        The `Delete` method:
        1. Connects to the Hyper-V host
        2. Gets the virtual machine by name
        3. Starts the VM (to ensure it's in a state that can be properly deleted)
        4. Gracefully stops the VM
        5. Deletes the virtual machine

        ## Available Properties

        | Property | Type | Description | Default |
        |----------|------|-------------|---------|
        | `machineName` | string | Name of the Virtual Machine | (required) |
        | `generation` | int | Generation of the Virtual Machine (1 or 2) | 2 |
        | `processorCount` | int | Number of processors to allocate | 1 |
        | `memorySize` | int | Memory size in MB | 1024 |
        | `dynamicMemory` | bool | Enable dynamic memory for the VM | false |
        | `minimumMemory` | int | Minimum memory in MB when using dynamic memory | - |
        | `maximumMemory` | int | Maximum memory in MB when using dynamic memory | - |
        | `autoStartAction` | string | Action on host start (Nothing, StartIfRunning, Start) | Nothing |
        | `autoStopAction` | string | Action on host shutdown (TurnOff, Save, ShutDown) | TurnOff |
        | `networkAdapters` | array | Network adapters to attach to the VM | [] |
        | `hardDrives` | array | Hard drives to attach to the VM | [] |
        | `triggers` | array | Values that trigger resource replacement when changed | (optional) |

        ### Network Adapter Properties

        | Property | Type | Description | Default |
        |----------|------|-------------|---------|
        | `name` | string | Name of the network adapter | "Network Adapter" |
        | `switchName` | string | Name of the virtual switch to connect to | (required) |

        ### Hard Drive Properties

        | Property | Type | Description | Default |
        |----------|------|-------------|---------|
        | `path` | string | Path to the VHD/VHDX file | (required) |
        | `controllerType` | string | Type of controller (IDE or SCSI) | SCSI |
        | `controllerNumber` | int | Controller number | 0 |
        | `controllerLocation` | int | Controller location | 0 |

        ## Usage Examples

        ## Related Documentation

        - [Microsoft Hyper-V Documentation](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-on-windows-server)
        - [Pulumi Hyper-V Provider Documentation](https://www.pulumi.com/registry/packages/hyperv/)

        :param str resource_name: The name of the resource.
        :param MachineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MachineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_start_action: Optional[pulumi.Input[builtins.str]] = None,
                 auto_stop_action: Optional[pulumi.Input[builtins.str]] = None,
                 create: Optional[pulumi.Input[builtins.str]] = None,
                 delete: Optional[pulumi.Input[builtins.str]] = None,
                 dynamic_memory: Optional[pulumi.Input[builtins.bool]] = None,
                 generation: Optional[pulumi.Input[builtins.int]] = None,
                 hard_drives: Optional[pulumi.Input[Sequence[pulumi.Input[Union['HardDriveInputArgs', 'HardDriveInputArgsDict']]]]] = None,
                 machine_name: Optional[pulumi.Input[builtins.str]] = None,
                 maximum_memory: Optional[pulumi.Input[builtins.int]] = None,
                 memory_size: Optional[pulumi.Input[builtins.int]] = None,
                 minimum_memory: Optional[pulumi.Input[builtins.int]] = None,
                 network_adapters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['_networkadapter.NetworkAdapterInputsArgs', '_networkadapter.NetworkAdapterInputsArgsDict']]]]] = None,
                 processor_count: Optional[pulumi.Input[builtins.int]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 update: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MachineArgs.__new__(MachineArgs)

            __props__.__dict__["auto_start_action"] = auto_start_action
            __props__.__dict__["auto_stop_action"] = auto_stop_action
            __props__.__dict__["create"] = create
            __props__.__dict__["delete"] = delete
            __props__.__dict__["dynamic_memory"] = dynamic_memory
            __props__.__dict__["generation"] = generation
            __props__.__dict__["hard_drives"] = hard_drives
            __props__.__dict__["machine_name"] = machine_name
            __props__.__dict__["maximum_memory"] = maximum_memory
            __props__.__dict__["memory_size"] = memory_size
            __props__.__dict__["minimum_memory"] = minimum_memory
            __props__.__dict__["network_adapters"] = network_adapters
            __props__.__dict__["processor_count"] = processor_count
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["update"] = update
            __props__.__dict__["vm_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["networkAdapters[*].triggers[*]", "triggers[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Machine, __self__).__init__(
            'hyperv:machine:Machine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Machine':
        """
        Get an existing Machine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MachineArgs.__new__(MachineArgs)

        __props__.__dict__["auto_start_action"] = None
        __props__.__dict__["auto_stop_action"] = None
        __props__.__dict__["create"] = None
        __props__.__dict__["delete"] = None
        __props__.__dict__["dynamic_memory"] = None
        __props__.__dict__["generation"] = None
        __props__.__dict__["hard_drives"] = None
        __props__.__dict__["machine_name"] = None
        __props__.__dict__["maximum_memory"] = None
        __props__.__dict__["memory_size"] = None
        __props__.__dict__["minimum_memory"] = None
        __props__.__dict__["network_adapters"] = None
        __props__.__dict__["processor_count"] = None
        __props__.__dict__["triggers"] = None
        __props__.__dict__["update"] = None
        __props__.__dict__["vm_id"] = None
        return Machine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoStartAction")
    def auto_start_action(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The action to take when the host starts. Valid values are Nothing, StartIfRunning, and Start. Defaults to Nothing.
        """
        return pulumi.get(self, "auto_start_action")

    @property
    @pulumi.getter(name="autoStopAction")
    def auto_stop_action(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The action to take when the host shuts down. Valid values are TurnOff, Save, and ShutDown. Defaults to TurnOff.
        """
        return pulumi.get(self, "auto_stop_action")

    @property
    @pulumi.getter
    def create(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The command to run on create.
        """
        return pulumi.get(self, "create")

    @property
    @pulumi.getter
    def delete(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
        and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
        Command resource from previous create or update steps.
        """
        return pulumi.get(self, "delete")

    @property
    @pulumi.getter(name="dynamicMemory")
    def dynamic_memory(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Whether to enable dynamic memory for the Virtual Machine. Defaults to false.
        """
        return pulumi.get(self, "dynamic_memory")

    @property
    @pulumi.getter
    def generation(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Generation of the Virtual Machine. Defaults to 2.
        """
        return pulumi.get(self, "generation")

    @property
    @pulumi.getter(name="hardDrives")
    def hard_drives(self) -> pulumi.Output[Optional[Sequence['outputs.HardDriveInput']]]:
        """
        Hard drives to attach to the Virtual Machine.
        """
        return pulumi.get(self, "hard_drives")

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Name of the Virtual Machine
        """
        return pulumi.get(self, "machine_name")

    @property
    @pulumi.getter(name="maximumMemory")
    def maximum_memory(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Maximum amount of memory that can be allocated to the Virtual Machine in MB when using dynamic memory.
        """
        return pulumi.get(self, "maximum_memory")

    @property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Amount of memory to allocate to the Virtual Machine in MB. Defaults to 1024.
        """
        return pulumi.get(self, "memory_size")

    @property
    @pulumi.getter(name="minimumMemory")
    def minimum_memory(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Minimum amount of memory to allocate to the Virtual Machine in MB when using dynamic memory.
        """
        return pulumi.get(self, "minimum_memory")

    @property
    @pulumi.getter(name="networkAdapters")
    def network_adapters(self) -> pulumi.Output[Optional[Sequence['_networkadapter.outputs.NetworkAdapterInputs']]]:
        """
        Network adapters to attach to the Virtual Machine.
        """
        return pulumi.get(self, "network_adapters")

    @property
    @pulumi.getter(name="processorCount")
    def processor_count(self) -> pulumi.Output[Optional[builtins.int]]:
        """
        Number of processors to allocate to the Virtual Machine. Defaults to 1.
        """
        return pulumi.get(self, "processor_count")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Trigger a resource replacement on changes to any of these values. The
        trigger values can be of any type. If a value is different in the current update compared to the
        previous update, the resource will be replaced, i.e., the "create" command will be re-run.
        Please see the resource documentation for examples.
        """
        return pulumi.get(self, "triggers")

    @property
    @pulumi.getter
    def update(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The command to run on update, if empty, create will 
        run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
        are set to the stdout and stderr properties of the Command resource from previous 
        create or update steps.
        """
        return pulumi.get(self, "update")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "vm_id")

