# example-codegen

An example repository to demonstrate codegen support in Pants. 

Refer to these docs for more information:

* [Python Protobuf](https://www.pantsbuild.org/v2.10/docs/protobuf-python)
* [Python Thrift](https://www.pantsbuild.org/v2.10/docs/thrift-python)

Run `./pants export-codegen ::` to see the generated files. This isn't necessary for Pants to 
use the generated files, but can be useful when debugging or to generate files for IDEs.

Check out our other [example repositories](https://www.pantsbuild.org/docs/example-repos) to see 
other features like running linters and formatters, and packaging binaries.
