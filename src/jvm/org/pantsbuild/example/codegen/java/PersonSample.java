package org.pantsbuild.example.codegen.java;

import org.pantsbuild.example.codegen.protos.Person;

public class PersonSample {
  public static void main(String[] args) {
    Person p = Person.newBuilder()
      .setName("Someone")
      .setId(1234)
      .setEmail("someone@example.com")
      .build();
    System.out.println(p);
  }
}

