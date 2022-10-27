// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Copy a local file to a remote host.
 */
export class CopyFile extends pulumi.CustomResource {
    /**
     * Get an existing CopyFile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CopyFile {
        return new CopyFile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'command:remote:CopyFile';

    /**
     * Returns true if the given object is an instance of CopyFile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CopyFile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CopyFile.__pulumiType;
    }

    /**
     * The parameters with which to connect to the remote host.
     */
    public readonly connection!: pulumi.Output<outputs.remote.Connection>;
    /**
     * The path of the file to be copied.
     */
    public readonly localPath!: pulumi.Output<string>;
    /**
     * The destination path in the remote host.
     */
    public readonly remotePath!: pulumi.Output<string>;
    /**
     * Trigger replacements on changes to this input.
     */
    public readonly triggers!: pulumi.Output<any[] | undefined>;

    /**
     * Create a CopyFile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CopyFileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.connection === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connection'");
            }
            if ((!args || args.localPath === undefined) && !opts.urn) {
                throw new Error("Missing required property 'localPath'");
            }
            if ((!args || args.remotePath === undefined) && !opts.urn) {
                throw new Error("Missing required property 'remotePath'");
            }
            resourceInputs["connection"] = args?.connection ? pulumi.secret((args.connection ? pulumi.output(args.connection).apply(inputs.remote.connectionArgsProvideDefaults) : undefined)) : undefined;
            resourceInputs["localPath"] = args ? args.localPath : undefined;
            resourceInputs["remotePath"] = args ? args.remotePath : undefined;
            resourceInputs["triggers"] = args ? args.triggers : undefined;
        } else {
            resourceInputs["connection"] = undefined /*out*/;
            resourceInputs["localPath"] = undefined /*out*/;
            resourceInputs["remotePath"] = undefined /*out*/;
            resourceInputs["triggers"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["connection"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(CopyFile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CopyFile resource.
 */
export interface CopyFileArgs {
    /**
     * The parameters with which to connect to the remote host.
     */
    connection: pulumi.Input<inputs.remote.ConnectionArgs>;
    /**
     * The path of the file to be copied.
     */
    localPath: pulumi.Input<string>;
    /**
     * The destination path in the remote host.
     */
    remotePath: pulumi.Input<string>;
    /**
     * Trigger replacements on changes to this input.
     */
    triggers?: pulumi.Input<any[]>;
}
