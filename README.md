# Python Application for OpenShift

## Overview

This project demonstrates deploying a Python application on OpenShift using GitHub Actions for CI, Harness for CD, Buildpacks for containerization, and HashiCorp Vault for secret management.

## Features

- **Containerization with Buildpacks**: No manual Dockerfile required.
- **Secrets Management**: Securely fetch secrets using HashiCorp Vault.
- **CI/CD Pipelines**: Automate build, test, and deployment with GitHub Actions and Harness.
- **Monitoring and Logging**: Includes a sidecar container for observability.

## Prerequisites

- OpenShift Cluster
- GitHub and Harness accounts
- HashiCorp Vault
- Docker Registry
- Buildpacks CLI (`pack`)

## Setup and Deployment

### Build and Push Image

```bash
pack build <your-registry>/python-app:latest --builder paketobuildpacks/builder:base
docker push <your-registry>/python-app:latest
