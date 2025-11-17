<h1 align="center">Dev Container Templates</h1>

<p align="center">
  <a href="https://github.com/e-gineering/devcontainer-templates/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
  <a href="https://containers.dev">
    <img src="https://img.shields.io/badge/Dev%20Containers-Specification-blue" alt="Dev Containers">
  </a>
</p>

<p align="center">
  A collection of Dev Container Templates for streamlined development environments.
</p>

---

## Overview

This repository contains Dev Container Templates that provide pre-configured development environments. These templates follow the [Dev Container specification](https://containers.dev/) and can be used with Visual Studio Code, GitHub Codespaces, or any other Dev Container-compatible tool.

## Quick Start

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or a compatible container runtime
- [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), OR
- [GitHub Codespaces](https://github.com/features/codespaces)

### Using a Template

1. In VS Code, open the Command Palette (`F1` or `Ctrl+Shift+P`)
2. Select "Dev Containers: Add Dev Container Configuration Files..."
3. Choose "Add configuration to workspace"
4. Select "Show All Definitions..."
5. Search for the template you want to use (e.g., "Fabric Runtime")
6. Select the template and configure any options
7. VS Code will create a `.devcontainer` folder with the configuration
8. Reopen the workspace in the container using "Dev Containers: Reopen in Container"

Alternatively, you can manually create a `.devcontainer/devcontainer.json` file in your project using the examples provided in the template documentation below.

## Available Templates

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

---

## Contributing

Contributions are welcome! If you'd like to add a new template or improve an existing one:

1. Fork the repository
2. Create a new branch for your changes
3. Add or modify templates in the `src/` directory
4. Test your changes locally
5. Submit a pull request

### Template Structure

Each template should follow this structure:

```
src/
└── your-template-name/
    ├── devcontainer-template.json    # Template metadata and options
    ├── .devcontainer/
    │   └── devcontainer.json         # Dev container configuration
    └── README.md                     # Template documentation (auto-generated)
```

The `devcontainer-template.json` file should include:
- `id`: Unique identifier for the template
- `version`: Template version (semver)
- `name`: Display name
- `description`: Brief description
- `options`: Configuration options for the template
- `platforms`: Supported platforms

## Resources

- [Dev Containers Documentation](https://containers.dev/)
- [Dev Containers Specification](https://github.com/devcontainers/spec)
- [VS Code Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [Dev Container Images Repository](https://github.com/e-gineering/devcontainer-images)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This repository structure is based on the [Dev Container Templates](https://github.com/devcontainers/templates) specification and follows the official Dev Container template format.
