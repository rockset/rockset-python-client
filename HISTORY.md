### v0.1.10
    - Undo renaming of integration creation operations

### v0.1.9
    - Use us-east-1 as default region

### v0.1.8
    - Change delete users to use short name

### v0.1.7
    - Allow nulls for values without removing

### v0.1.6
    - Use init during preparation

### v0.1.5
    - Add query_response.py back

### v0.1.4
    - Delete old models

### v0.1.3
    - Fix for read-only deserialization

### v0.1.2
    - Fix recursive version of deserialization bug

### v0.1.1
    - Fix for deserialization bug

### v0.1.0
    - Rename standard operations
    - Allow for dictionaries to be passed in instead of fully-instantiated objects
    - Simplify collection source object structure

### v0.0.17
    - Fix bug where query parameters were not being propagated to the actual call.
    - Add the QueryPaginator class which can be used as an iterator for paginated queries.

### v0.0.16
    - Ignore nulls when deserializing responses so type validation succeeds

### v0.0.15
    - Introduce temporary fix for nullable enums

### v0.0.14
    - Allow none for fields inside of response objects

### v0.0.13
    - Fix bug that occurs when no parameters are passed in to sql()

### v0.0.12
    - Updates for latest API changes (namely removal of the updateIntegration call)

### v0.0.11
    - Add convenience method for making queries (rs.sql()).
    - Port over code from the old client's query builder.

### v0.0.10
    - Include response type-checking and nested object model object conversions by default.

### v0.0.9
    - Bug fixes
    - Change pattern of API groups (AliasesApi -> Aliases)

### v0.0.8
    - Ease-of-use upgrades for host initialization
    - Typo fixes

### v0.0.7
    - Update client for async options
    - Update readme
    - Remove unnecessary imports

### v0.0.6
    - Update client for API updates

### v0.0.5
    - Reintroduce correct formatting for code examples in docstrings

### v0.0.4
    - More updates for extra files

### v0.0.3
    - Add long description file

### v0.0.2
    - Update pyproject.toml to include all dependencies
    - Add release information

### v0.0.1
    - Initial release