package examples

import "testing"
import "github.com/pantsbuild/example-codegen/gen"

func TestGenerateUuid(t *testing.T) {
	person := gen.Person{
		Name:  "Thomas the Train",
		Id:    1,
		Email: "allaboard@trains.build",
	}
	if person.Name != "Thomas the Train" {
		t.Fail()
	}
}
