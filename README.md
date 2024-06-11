<h1 align="center">Dev Container Templates</h1>

## Templates

<!-- START_TEMPLATES -->

### Fabric Runtime (fabric-runtime)

Mimics the Microsoft Fabric Runtime for local development of PySpark notebooks.

#### Options

| Options Id | Description | Type | Default Value |
|-----|-----|-----|-----|
| imageVariant | Version of the Fabric Runtime to use | string | 1.2 |

#### Using this template

Get started with a `.devcontainer/devcontainer.json` like:

```json
{
  "name": "Fabric Runtime 1.2",
  "image": "ghcr.io/e-gineering/devcontainer-images/fabric-runtime:1.2"
}
```

Or install some additional Python packages by creating a `.devcontainer/requirements.txt` and installing them with:

```json
{
  "name": "Fabric Runtime 1.2",
  "image": "ghcr.io/e-gineering/devcontainer-images/fabric-runtime:1.2",
  "onCreateCommand": "pip install -r .devcontainer/requirements.txt"
}
```

#### About

These images are created with PySpark workloads in mind, so you'll find Python and Java installed, but not Scala or R at this point.

You can find the image sources here: https://github.com/e-gineering/devcontainer-images/tree/main/src/fabric-runtime

#### Software versions

The software versions are pinned to track the versions listed in the Microsoft [docs](https://learn.microsoft.com/en-us/fabric/data-engineering/runtime).

##### Fabric Runtime 1.3

- Apache Spark 3.5.1
- Java 11
- Python 3.11
- Delta Lake 3.1.0

Microsoft docs for 1.3: https://learn.microsoft.com/en-us/fabric/data-engineering/runtime-1-3

##### Fabric Runtime 1.2

- Apache Spark 3.4.1
- Java 11
- Python 3.10
- Delta Lake 2.4.0

Microsoft docs for 1.2: https://learn.microsoft.com/en-us/fabric/data-engineering/runtime-1-2

##### Fabric Runtime 1.1

- Apache Spark 3.3.1
- Java 8
- Python 3.10
- Delta Lake 2.2.0

Microsoft docs for 1.1: https://learn.microsoft.com/en-us/fabric/data-engineering/runtime-1-1

<!-- END_TEMPLATES -->
