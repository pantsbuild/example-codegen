from simple_example.v1.person_pb2 import Person

def test_person() -> None:
  p = Person()
  p.name = "Me"
  p.id = 3
  p.email = "me@example.com"
  assert p.name == "Me"
  assert p.id == 3
  assert p.email == "me@example.com"

