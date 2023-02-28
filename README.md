# example-codegen

An example repository to demonstrate codegen support in Pants. 

You run Pants goals using the `pants` launcher binary, which will bootstrap the
version of Pants configured for this repo if necessary.

See [here](https://www.pantsbuild.org/docs/installation) for how to install the `pants` binary.

Refer to these docs for more information:

* [Go Protobuf](https://www.pantsbuild.org/docs/protobuf-go)
* [Python Protobuf](https://www.pantsbuild.org/docs/protobuf-python)
* [Python Thrift](https://www.pantsbuild.org/docs/thrift-python)

Some commands you can try out:

* `pants export-codegen ::` - see the generated files.
    * This isn't necessary for Pants to use the generated files, but can be useful when
      debugging or to generate files for IDEs.
* `pants test ::` - run all tests
* `pants fmt ::` - format Protobuf with `buf`
* `pants lint ::` - lint Protobuf with `buf`
* `pants dependencies <path/to/file>` - see what depends on what

Check out our other [example repositories](https://www.pantsbuild.org/docs/example-repos) to see 
other features like packaging binaries.

Note: to try out Go, you must comment out `pants_ignore` in `pants.toml`. This is so that non-Go 
users do not need to have Go installed to run the project.
