# Note: Apache Thrift generates mutiple Python packages from a single Thrift file. The base name
# of those packages comes from the value of the `namespace` directive in the Thrift file.
# `constants` and `ttypes` subpackages are generated under that base name.
#
# In this case, the `namespace` directive is `thrift_example.gen`. This, Apache Thrift generates two
# packages: `thrift_example.gen.constants` and `thrift_example.gen.ttypes`. This file then imports
# the `Person` class from `thrift_example.gen.ttypes`.

from thrift_example.gen.ttypes import Person

def test_person() -> None:
  p = Person("Me", 3, "me@example.com")
  assert p.name == "Me"

