// Copyright 2016-2022, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi-go-provider/middleware/schema"
	"github.com/pulumi/pulumi-hyperv-provider/provider/pkg/provider/vm"
)

const (
	Name = "hyperv"
)

// This provider uses the `pulumi-go-provider` library to produce a code-first provider definition.
func NewProvider() p.Provider {
	return infer.Provider(infer.Options{
		// This is the metadata for the provider
		Metadata: schema.Metadata{
			DisplayName: "Hyperv",
			Description: "The Pulumi hyperv Provider enables you to use Hyper-V resources in your Pulumi programs.",
			Keywords: []string{
				"pulumi",
				"hyperv",
				"category/utility",
				"kind/native",
			},
			Homepage:   "https://pulumi.com",
			License:    "Apache-2.0",
			Repository: "https://github.com/pulumi/pulumi-hyperv-provider",
			Publisher:  "Pulumi",
			LogoURL:    "https://raw.githubusercontent.com/pulumi/pulumi-hyperv-provider/master/assets/logo.svg",
			// This contains language specific details for generating the provider's SDKs
			LanguageMap: map[string]any{
				"csharp": map[string]any{
					"respectSchemaVersion": true,
					"packageReferences": map[string]string{
						"Pulumi": "3.*",
					},
				},
				"go": map[string]any{
					"respectSchemaVersion":           true,
					"generateResourceContainerTypes": true,
					"importBasePath":                 "github.com/pulumi/pulumi-hyperv-provider/provider/go/hyperv",
				},
				"nodejs": map[string]any{
					"respectSchemaVersion": true,
				},
				"python": map[string]any{
					"respectSchemaVersion": true,
					"pyproject": map[string]bool{
						"enabled": true,
					},
				},
				"java": map[string]any{
					"buildFiles":                      "gradle",
					"gradleNexusPublishPluginVersion": "2.0.0",
					"dependencies": map[string]any{
						"com.pulumi:pulumi":               "1.0.0",
						"com.google.code.gson:gson":       "2.8.9",
						"com.google.code.findbugs:jsr305": "3.0.2",
					},
				},
			},
		},
		// A list of `infer.Resource` that are provided by the provider.
		Resources: []infer.InferredResource{
			// The hyperv resource implementation is commented extensively for new pulumi-go-provider developers.
			infer.Resource[
				// 1. This type is an interface that implements the logic for the Resource
				//    these methods include `Create`, `Update`, `Delete`, and `WireDependencies`.
				//    `WireDependencies` should be implemented to preserve the secretness of an input
				*vm.Vm,
				// 2. The type of the Inputs/Arguments to supply to the Resource.
				vm.VmInputs,
				// 3. The type of the Output/Properties/Fields of a created Resource.
				vm.VmOutputs,
			](),
		},
		// Functions or invokes that are provided by the provider.
		Functions: []infer.InferredFunction{
			// The Run function is commented extensively for new pulumi-go-provider developers.
			infer.Function[*vm.Run, vm.RunInputs, vm.RunOutputs](),
		},
	})
}
