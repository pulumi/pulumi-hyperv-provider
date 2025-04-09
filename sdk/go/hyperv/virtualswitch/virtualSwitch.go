// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package virtualswitch

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-hyperv-provider/provider/go/hyperv/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// # Virtual Switch Resource Management
//
// The `virtualswitch` package provides utilities for managing Hyper-V virtual switches.
//
// ## Overview
//
// This package enables creating, modifying, and deleting virtual switches through the Pulumi Hyper-V provider. Virtual switches enable network connectivity for virtual machines.
//
// ## Key Components
//
// ### Types
//
// - **VirtualSwitch**: Represents a Hyper-V virtual switch.
//
// ### Resource Lifecycle Methods
//
// - **Create**: Creates a new virtual switch with specified properties.
// - **Read**: Retrieves information about an existing virtual switch.
// - **Update**: Modifies properties of an existing virtual switch.
// - **Delete**: Removes a virtual switch.
//
// ## Available Properties
//
// The VirtualSwitch resource supports the following properties:
//
// | Property | Type | Description |
// |----------|------|-------------|
// | `name` | string | Name of the virtual switch |
// | `switchType` | string | Type of switch: "External", "Internal", or "Private" |
// | `allowManagementOs` | boolean | Allow the management OS to access the switch (External switches) |
// | `netAdapterName` | string | Name of the physical network adapter to bind to (External switches) |
//
// ## Implementation Details
//
// The package uses the WMI interface to interact with Hyper-V's virtual switch management functionality, providing a Go-based interface that integrates with the Pulumi resource model.
//
// ## Usage Examples
//
// Virtual switches can be defined and managed through the Pulumi Hyper-V provider using the standard resource model.
//
// ### Creating an External Switch
//
// ### Creating an Internal Switch
type VirtualSwitch struct {
	pulumi.CustomResourceState

	// Allow the management OS to access the switch (External switches)
	AllowManagementOs pulumi.BoolPtrOutput `pulumi:"allowManagementOs"`
	// The command to run on create.
	Create pulumi.StringPtrOutput `pulumi:"create"`
	// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
	// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
	// Command resource from previous create or update steps.
	Delete pulumi.StringPtrOutput `pulumi:"delete"`
	// Name of the virtual switch
	Name pulumi.StringOutput `pulumi:"name"`
	// Name of the physical network adapter to bind to (External switches)
	NetAdapterName pulumi.StringPtrOutput `pulumi:"netAdapterName"`
	// Notes or description for the virtual switch
	Notes pulumi.StringPtrOutput `pulumi:"notes"`
	// Type of switch: 'External', 'Internal', or 'Private'
	SwitchType pulumi.StringOutput `pulumi:"switchType"`
	// Trigger a resource replacement on changes to any of these values. The
	// trigger values can be of any type. If a value is different in the current update compared to the
	// previous update, the resource will be replaced, i.e., the "create" command will be re-run.
	// Please see the resource documentation for examples.
	Triggers pulumi.ArrayOutput `pulumi:"triggers"`
	// The command to run on update, if empty, create will
	// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
	// are set to the stdout and stderr properties of the Command resource from previous
	// create or update steps.
	Update pulumi.StringPtrOutput `pulumi:"update"`
}

// NewVirtualSwitch registers a new resource with the given unique name, arguments, and options.
func NewVirtualSwitch(ctx *pulumi.Context,
	name string, args *VirtualSwitchArgs, opts ...pulumi.ResourceOption) (*VirtualSwitch, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.SwitchType == nil {
		return nil, errors.New("invalid value for required argument 'SwitchType'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"triggers[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VirtualSwitch
	err := ctx.RegisterResource("hyperv:virtualswitch:VirtualSwitch", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVirtualSwitch gets an existing VirtualSwitch resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualSwitch(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VirtualSwitchState, opts ...pulumi.ResourceOption) (*VirtualSwitch, error) {
	var resource VirtualSwitch
	err := ctx.ReadResource("hyperv:virtualswitch:VirtualSwitch", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VirtualSwitch resources.
type virtualSwitchState struct {
}

type VirtualSwitchState struct {
}

func (VirtualSwitchState) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualSwitchState)(nil)).Elem()
}

type virtualSwitchArgs struct {
	// Allow the management OS to access the switch (External switches)
	AllowManagementOs *bool `pulumi:"allowManagementOs"`
	// The command to run on create.
	Create *string `pulumi:"create"`
	// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
	// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
	// Command resource from previous create or update steps.
	Delete *string `pulumi:"delete"`
	// Name of the virtual switch
	Name string `pulumi:"name"`
	// Name of the physical network adapter to bind to (External switches)
	NetAdapterName *string `pulumi:"netAdapterName"`
	// Notes or description for the virtual switch
	Notes *string `pulumi:"notes"`
	// Type of switch: 'External', 'Internal', or 'Private'
	SwitchType string `pulumi:"switchType"`
	// Trigger a resource replacement on changes to any of these values. The
	// trigger values can be of any type. If a value is different in the current update compared to the
	// previous update, the resource will be replaced, i.e., the "create" command will be re-run.
	// Please see the resource documentation for examples.
	Triggers []interface{} `pulumi:"triggers"`
	// The command to run on update, if empty, create will
	// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
	// are set to the stdout and stderr properties of the Command resource from previous
	// create or update steps.
	Update *string `pulumi:"update"`
}

// The set of arguments for constructing a VirtualSwitch resource.
type VirtualSwitchArgs struct {
	// Allow the management OS to access the switch (External switches)
	AllowManagementOs pulumi.BoolPtrInput
	// The command to run on create.
	Create pulumi.StringPtrInput
	// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
	// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
	// Command resource from previous create or update steps.
	Delete pulumi.StringPtrInput
	// Name of the virtual switch
	Name pulumi.StringInput
	// Name of the physical network adapter to bind to (External switches)
	NetAdapterName pulumi.StringPtrInput
	// Notes or description for the virtual switch
	Notes pulumi.StringPtrInput
	// Type of switch: 'External', 'Internal', or 'Private'
	SwitchType pulumi.StringInput
	// Trigger a resource replacement on changes to any of these values. The
	// trigger values can be of any type. If a value is different in the current update compared to the
	// previous update, the resource will be replaced, i.e., the "create" command will be re-run.
	// Please see the resource documentation for examples.
	Triggers pulumi.ArrayInput
	// The command to run on update, if empty, create will
	// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
	// are set to the stdout and stderr properties of the Command resource from previous
	// create or update steps.
	Update pulumi.StringPtrInput
}

func (VirtualSwitchArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualSwitchArgs)(nil)).Elem()
}

type VirtualSwitchInput interface {
	pulumi.Input

	ToVirtualSwitchOutput() VirtualSwitchOutput
	ToVirtualSwitchOutputWithContext(ctx context.Context) VirtualSwitchOutput
}

func (*VirtualSwitch) ElementType() reflect.Type {
	return reflect.TypeOf((**VirtualSwitch)(nil)).Elem()
}

func (i *VirtualSwitch) ToVirtualSwitchOutput() VirtualSwitchOutput {
	return i.ToVirtualSwitchOutputWithContext(context.Background())
}

func (i *VirtualSwitch) ToVirtualSwitchOutputWithContext(ctx context.Context) VirtualSwitchOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VirtualSwitchOutput)
}

// VirtualSwitchArrayInput is an input type that accepts VirtualSwitchArray and VirtualSwitchArrayOutput values.
// You can construct a concrete instance of `VirtualSwitchArrayInput` via:
//
//	VirtualSwitchArray{ VirtualSwitchArgs{...} }
type VirtualSwitchArrayInput interface {
	pulumi.Input

	ToVirtualSwitchArrayOutput() VirtualSwitchArrayOutput
	ToVirtualSwitchArrayOutputWithContext(context.Context) VirtualSwitchArrayOutput
}

type VirtualSwitchArray []VirtualSwitchInput

func (VirtualSwitchArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VirtualSwitch)(nil)).Elem()
}

func (i VirtualSwitchArray) ToVirtualSwitchArrayOutput() VirtualSwitchArrayOutput {
	return i.ToVirtualSwitchArrayOutputWithContext(context.Background())
}

func (i VirtualSwitchArray) ToVirtualSwitchArrayOutputWithContext(ctx context.Context) VirtualSwitchArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VirtualSwitchArrayOutput)
}

// VirtualSwitchMapInput is an input type that accepts VirtualSwitchMap and VirtualSwitchMapOutput values.
// You can construct a concrete instance of `VirtualSwitchMapInput` via:
//
//	VirtualSwitchMap{ "key": VirtualSwitchArgs{...} }
type VirtualSwitchMapInput interface {
	pulumi.Input

	ToVirtualSwitchMapOutput() VirtualSwitchMapOutput
	ToVirtualSwitchMapOutputWithContext(context.Context) VirtualSwitchMapOutput
}

type VirtualSwitchMap map[string]VirtualSwitchInput

func (VirtualSwitchMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VirtualSwitch)(nil)).Elem()
}

func (i VirtualSwitchMap) ToVirtualSwitchMapOutput() VirtualSwitchMapOutput {
	return i.ToVirtualSwitchMapOutputWithContext(context.Background())
}

func (i VirtualSwitchMap) ToVirtualSwitchMapOutputWithContext(ctx context.Context) VirtualSwitchMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VirtualSwitchMapOutput)
}

type VirtualSwitchOutput struct{ *pulumi.OutputState }

func (VirtualSwitchOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VirtualSwitch)(nil)).Elem()
}

func (o VirtualSwitchOutput) ToVirtualSwitchOutput() VirtualSwitchOutput {
	return o
}

func (o VirtualSwitchOutput) ToVirtualSwitchOutputWithContext(ctx context.Context) VirtualSwitchOutput {
	return o
}

// Allow the management OS to access the switch (External switches)
func (o VirtualSwitchOutput) AllowManagementOs() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.BoolPtrOutput { return v.AllowManagementOs }).(pulumi.BoolPtrOutput)
}

// The command to run on create.
func (o VirtualSwitchOutput) Create() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringPtrOutput { return v.Create }).(pulumi.StringPtrOutput)
}

// The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
// and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
// Command resource from previous create or update steps.
func (o VirtualSwitchOutput) Delete() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringPtrOutput { return v.Delete }).(pulumi.StringPtrOutput)
}

// Name of the virtual switch
func (o VirtualSwitchOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Name of the physical network adapter to bind to (External switches)
func (o VirtualSwitchOutput) NetAdapterName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringPtrOutput { return v.NetAdapterName }).(pulumi.StringPtrOutput)
}

// Notes or description for the virtual switch
func (o VirtualSwitchOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringPtrOutput { return v.Notes }).(pulumi.StringPtrOutput)
}

// Type of switch: 'External', 'Internal', or 'Private'
func (o VirtualSwitchOutput) SwitchType() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringOutput { return v.SwitchType }).(pulumi.StringOutput)
}

// Trigger a resource replacement on changes to any of these values. The
// trigger values can be of any type. If a value is different in the current update compared to the
// previous update, the resource will be replaced, i.e., the "create" command will be re-run.
// Please see the resource documentation for examples.
func (o VirtualSwitchOutput) Triggers() pulumi.ArrayOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.ArrayOutput { return v.Triggers }).(pulumi.ArrayOutput)
}

// The command to run on update, if empty, create will
// run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
// are set to the stdout and stderr properties of the Command resource from previous
// create or update steps.
func (o VirtualSwitchOutput) Update() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualSwitch) pulumi.StringPtrOutput { return v.Update }).(pulumi.StringPtrOutput)
}

type VirtualSwitchArrayOutput struct{ *pulumi.OutputState }

func (VirtualSwitchArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VirtualSwitch)(nil)).Elem()
}

func (o VirtualSwitchArrayOutput) ToVirtualSwitchArrayOutput() VirtualSwitchArrayOutput {
	return o
}

func (o VirtualSwitchArrayOutput) ToVirtualSwitchArrayOutputWithContext(ctx context.Context) VirtualSwitchArrayOutput {
	return o
}

func (o VirtualSwitchArrayOutput) Index(i pulumi.IntInput) VirtualSwitchOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *VirtualSwitch {
		return vs[0].([]*VirtualSwitch)[vs[1].(int)]
	}).(VirtualSwitchOutput)
}

type VirtualSwitchMapOutput struct{ *pulumi.OutputState }

func (VirtualSwitchMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VirtualSwitch)(nil)).Elem()
}

func (o VirtualSwitchMapOutput) ToVirtualSwitchMapOutput() VirtualSwitchMapOutput {
	return o
}

func (o VirtualSwitchMapOutput) ToVirtualSwitchMapOutputWithContext(ctx context.Context) VirtualSwitchMapOutput {
	return o
}

func (o VirtualSwitchMapOutput) MapIndex(k pulumi.StringInput) VirtualSwitchOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *VirtualSwitch {
		return vs[0].(map[string]*VirtualSwitch)[vs[1].(string)]
	}).(VirtualSwitchOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VirtualSwitchInput)(nil)).Elem(), &VirtualSwitch{})
	pulumi.RegisterInputType(reflect.TypeOf((*VirtualSwitchArrayInput)(nil)).Elem(), VirtualSwitchArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VirtualSwitchMapInput)(nil)).Elem(), VirtualSwitchMap{})
	pulumi.RegisterOutputType(VirtualSwitchOutput{})
	pulumi.RegisterOutputType(VirtualSwitchArrayOutput{})
	pulumi.RegisterOutputType(VirtualSwitchMapOutput{})
}
