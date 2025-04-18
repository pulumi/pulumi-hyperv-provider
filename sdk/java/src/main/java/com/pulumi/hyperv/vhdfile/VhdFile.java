// *** WARNING: this file was generated by pulumi-language-java. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.hyperv.vhdfile;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.hyperv.Utilities;
import com.pulumi.hyperv.vhdfile.VhdFileArgs;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * # VHD File Resource Management
 * 
 * The `vhdfile` package provides utilities for managing VHD (Virtual Hard Disk) files for Hyper-V virtual machines.
 * 
 * ## Overview
 * 
 * This package enables creating, modifying, and deleting VHD and VHDX files through the Pulumi Hyper-V provider. It provides a clean abstraction for working with virtual disk files independent of virtual machines.
 * 
 * ## Key Components
 * 
 * ### Types
 * 
 * - **VhdFile**: Represents a VHD or VHDX file for use with Hyper-V virtual machines.
 * 
 * ### Resource Lifecycle Methods
 * 
 * - **Create**: Creates a new VHD/VHDX file with specified properties.
 * - **Read**: Retrieves information about an existing VHD/VHDX file.
 * - **Update**: Modifies properties of an existing VHD/VHDX file (currently a no-op in the implementation).
 * - **Delete**: Removes a VHD/VHDX file.
 * 
 * ## Available Properties
 * 
 * The VhdFile resource supports the following properties:
 * 
 * | Property | Type | Description |
 * |----------|------|-------------|
 * | `path` | string | Path where the VHD file should be created |
 * | `parentPath` | string | Path to parent VHD when creating differencing disks |
 * | `diskType` | string | Type of disk (Fixed, Dynamic, Differencing) |
 * | `sizeBytes` | number | Size of the disk in bytes (for Fixed and Dynamic disks) |
 * | `blockSize` | number | Block size of the disk in bytes (recommended: 1048576 for 1MB) |
 * 
 * ## Implementation Details
 * 
 * The package uses PowerShell commands under the hood to interact with Hyper-V&#39;s VHD management functionality, providing a Go-based interface that integrates with the Pulumi resource model.
 * 
 * ### Update Behavior
 * 
 * The current implementation of the `Update` method is a no-op. Any changes to VHD properties that require modification of the underlying file structure will typically require replacing the resource rather than updating it in place.
 * 
 * ## Usage Examples
 * 
 * VHD files can be defined and managed through the Pulumi Hyper-V provider using the standard resource model. These virtual disks can then be attached to virtual machines or managed independently.
 * 
 * ### Creating a Base VHD
 * 
 * ### Creating a Differencing Disk
 * 
 * ### Using with Machine Resource
 * 
 * The VhdFile resource can be used in conjunction with the Machine resource by attaching the VHD files to a virtual machine using the `hardDrives` array:
 * 
 */
@ResourceType(type="hyperv:vhdfile:VhdFile")
public class VhdFile extends com.pulumi.resources.CustomResource {
    /**
     * Block size of the VHD file in bytes. Recommended value is 1MB (1048576 bytes) for better compatibility.
     * 
     */
    @Export(name="blockSize", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> blockSize;

    /**
     * @return Block size of the VHD file in bytes. Recommended value is 1MB (1048576 bytes) for better compatibility.
     * 
     */
    public Output<Optional<Integer>> blockSize() {
        return Codegen.optional(this.blockSize);
    }
    /**
     * The command to run on create.
     * 
     */
    @Export(name="create", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> create;

    /**
     * @return The command to run on create.
     * 
     */
    public Output<Optional<String>> create() {
        return Codegen.optional(this.create);
    }
    /**
     * The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
     * and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
     * Command resource from previous create or update steps.
     * 
     */
    @Export(name="delete", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> delete;

    /**
     * @return The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
     * and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
     * Command resource from previous create or update steps.
     * 
     */
    public Output<Optional<String>> delete() {
        return Codegen.optional(this.delete);
    }
    /**
     * Type of the VHD file (Fixed, Dynamic, or Differencing)
     * 
     */
    @Export(name="diskType", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> diskType;

    /**
     * @return Type of the VHD file (Fixed, Dynamic, or Differencing)
     * 
     */
    public Output<Optional<String>> diskType() {
        return Codegen.optional(this.diskType);
    }
    /**
     * Path to the parent VHD file when creating a differencing disk
     * 
     */
    @Export(name="parentPath", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> parentPath;

    /**
     * @return Path to the parent VHD file when creating a differencing disk
     * 
     */
    public Output<Optional<String>> parentPath() {
        return Codegen.optional(this.parentPath);
    }
    /**
     * Path to the VHD file
     * 
     */
    @Export(name="path", refs={String.class}, tree="[0]")
    private Output<String> path;

    /**
     * @return Path to the VHD file
     * 
     */
    public Output<String> path() {
        return this.path;
    }
    /**
     * Size of the VHD file in bytes
     * 
     */
    @Export(name="sizeBytes", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> sizeBytes;

    /**
     * @return Size of the VHD file in bytes
     * 
     */
    public Output<Optional<Integer>> sizeBytes() {
        return Codegen.optional(this.sizeBytes);
    }
    /**
     * Trigger a resource replacement on changes to any of these values. The
     * trigger values can be of any type. If a value is different in the current update compared to the
     * previous update, the resource will be replaced, i.e., the &#34;create&#34; command will be re-run.
     * Please see the resource documentation for examples.
     * 
     */
    @Export(name="triggers", refs={List.class,Object.class}, tree="[0,1]")
    private Output</* @Nullable */ List<Object>> triggers;

    /**
     * @return Trigger a resource replacement on changes to any of these values. The
     * trigger values can be of any type. If a value is different in the current update compared to the
     * previous update, the resource will be replaced, i.e., the &#34;create&#34; command will be re-run.
     * Please see the resource documentation for examples.
     * 
     */
    public Output<Optional<List<Object>>> triggers() {
        return Codegen.optional(this.triggers);
    }
    /**
     * The command to run on update, if empty, create will
     * run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
     * are set to the stdout and stderr properties of the Command resource from previous
     * create or update steps.
     * 
     */
    @Export(name="update", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> update;

    /**
     * @return The command to run on update, if empty, create will
     * run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
     * are set to the stdout and stderr properties of the Command resource from previous
     * create or update steps.
     * 
     */
    public Output<Optional<String>> update() {
        return Codegen.optional(this.update);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public VhdFile(java.lang.String name) {
        this(name, VhdFileArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public VhdFile(java.lang.String name, VhdFileArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public VhdFile(java.lang.String name, VhdFileArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("hyperv:vhdfile:VhdFile", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private VhdFile(java.lang.String name, Output<java.lang.String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("hyperv:vhdfile:VhdFile", name, null, makeResourceOptions(options, id), false);
    }

    private static VhdFileArgs makeArgs(VhdFileArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? VhdFileArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static VhdFile get(java.lang.String name, Output<java.lang.String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new VhdFile(name, id, options);
    }
}
