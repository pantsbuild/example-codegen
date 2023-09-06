protobuf_sources(
    # This will generate files under `src/python`, rather than `src/protobuf`, which is convenient
    # so that we do not need to add `__init__.py` files to `src/protobuf`. See
    # https://www.pantsbuild.org/docs/protobuf-python#protobuf-and-source-roots
    python_source_root="src/python",
    # TODO: Infer this. See https://github.com/pantsbuild/pants/issues/19766.
    dependencies=["3rdparty/python#types-protobuf"],
)
