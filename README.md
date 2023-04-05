# Open Source Reference

The purpose of this repository is provide a collection of reference materials in relation to open-source distributed multi agent systems development. 

The overarching goal of the repository is to eventually create an agent service capable of maintaining and improving itself.

We will initially accomplish this using the Valory Stack to create an agent service capable of reviewing pull requests created into the repository defining itself. 

In the short term, this allows the implementation of a simple frontend backend to ease managing a large number of repositories.

In the mid term, this will allow for much faster deployment and management of the repositories used as reference material.

In the long term, the goal is to construct a repostory capable of suggesting improvements to itself.

The stack is defined in skaffold, allowing the orchestration of a number of open source tools.

# Live Deployment

A live dashboard is provided at;

`https://dashy.rae.cloud`

This displays the current status of all of the applications and all current deployments.

- Repo Backend
- Repo Frontend
- Dashboard
- Status & Monitoring

## Deployment

### Terraform

Terraform is used to provision cloud resources.


### Skaffold

Skaffold is use to orchestrate a devployment to an existing cluster.

- Terraform
- Make

### Kubernetes

As a powerful container orchestration system, there are many different flavours of the kubernetes distribution.

Running bare-metal can be accomplished using kubeadm, however such a low level of deployment is inadvisable except under exceptional circumstances.


### Docker-Compose

Docker-compose is initially used to orchestrate local containers.
