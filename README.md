# sre-wordpress
# WordPress SRE Project


markdown

# WordPress SRE Project

A scalable WordPress deployment on AWS EKS with RDS, Lambda notifications, CloudWatch monitoring, and GitHub Actions CI/CD in us-east-1.

## Prerequisites
- AWS CLI, Terraform, kubectl, Helm, Docker, Git
- AWS account with EKS, RDS, ECR, Lambda, CloudWatch permissions
- GitHub repository

## Setup Instructions
1. **Clone Repository**:
   ```bash
   git clone https://github.com/shak1-1211/sre-wordpress.git
   cd sre-wordpress

Provision Infrastructure:

cd terraform
terraform init
terraform apply

Push Docker Image:

cd ../wordpress
docker build -t sre-wordpress .
docker tag sre-wordpress:latest 151287120928.dkr.ecr.us-east-1.amazonaws.com/sre-wordpress:latest
docker push 151287120928.dkr.ecr.us-east-1.amazonaws.com/sre-wordpress:latest

Deploy WordPress:
cd ..
helm install wordpress ./helm-chart

Set Up Lambda and Monitoring:
Follow lambda/ and monitoring/ instructions.

Configure CI/CD:
Add AWS secrets to GitHub Actions.

Testing
Access: kubectl port-forward svc/wordpress 8080:80

Create a post, verify Lambda notification.

Check CloudWatch alarms.


