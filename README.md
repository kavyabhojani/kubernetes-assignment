# Kubernetes Infrastructure Setup Assignment

This project demonstrates the deployment of a containerized application on a Kubernetes cluster using YAML configuration files for container setup and Terraform for infrastructure provisioning. The project includes Persistent Volume Claims (PVC) for managing storage, as well as deployment configurations for containers.

## Project Overview

This assignment focuses on deploying a multi-container application using Kubernetes. The key components include:

- **YAML configuration files** for deploying the containers and managing services.
- **Persistent Volume Claims (PVC)** for handling dynamic storage.
- **Terraform** for automating the provisioning of infrastructure resources.

## Files Included

- `container1-deployment.yaml` : Kubernetes configuration for the deployment of the first container.
- `container2-deployment.yaml` : Kubernetes configuration for the deployment of the second container.
- `kavya-pvc.yml` : YAML file to manage persistent volume claims (PVC).
- `main.tf` : Terraform script to provision the necessary infrastructure for Kubernetes.

## Prerequisites

- Kubernetes Cluster (Minikube, AWS EKS, GCP GKE, etc.)
- Terraform (v1.0+)
- Docker (for building images if necessary)
- kubectl (Kubernetes CLI)
- A cloud provider setup for provisioning resources

## Setup Instructions

1. **Set Up Kubernetes Cluster**:
   Ensure your Kubernetes cluster is up and running. You can use Minikube, AWS EKS, or any Kubernetes provider of your choice.

2. **Deploy Containers**:
   Apply the YAML configuration files to deploy the containers:
   ```bash
   kubectl apply -f container1-deployment.yaml
   kubectl apply -f container2-deployment.yaml
