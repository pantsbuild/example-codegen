# Note: Apache Thrift generates mutiple Python packages from a single Thrift file.
# `constants` and `ttypes` subpackages are generated under that base name. The base name
# of those packages comes from the value of the following `namespace` directive:
namespace py thrift_example.gen

struct Person {
  1: string name
  2: i32 id
  3: string email
}
