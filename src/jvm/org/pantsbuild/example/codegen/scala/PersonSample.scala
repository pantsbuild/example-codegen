package org.pantsbuild.example.codegen.scala

import org.pantsbuild.example.codegen.protos.person.Person

object PersonSample {
  def main(args: Array[String]): Unit = {
    val p = Person(
      name = "Someone",
      id = 1234,
      email = "someone@example.com",
    )
    println(p)
  }
}

