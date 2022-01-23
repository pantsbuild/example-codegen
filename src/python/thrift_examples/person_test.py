from thrift_example.gen.ttypes import Person

def test_person() -> None:
  p = Person("Me", 3, "me@example.com")
  assert p.name == "Me"

