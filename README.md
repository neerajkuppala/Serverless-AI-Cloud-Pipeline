🚀 Serverless Cloud Dashboard: Infrastructure-as-Code Project
Executive Summary
This project demonstrates a production-ready Serverless Microservice architecture deployed on Amazon Web Services (AWS) using Terraform. The system features a high-performance web dashboard that interacts with cloud storage through secure, temporary access protocols.

🏗️ Technical Architecture
Infrastructure as Code (IaC): Utilized Terraform to manage the full resource lifecycle, ensuring 100% reproducible environments and preventing configuration drift.

Compute: Implemented AWS Lambda (Python 3.11) to handle backend logic on a per-request basis, significantly reducing operational costs compared to traditional servers.

API Management: Configured Amazon API Gateway to provide a secure, scalable entry point for the web dashboard.

Storage & Security: Leveraged Amazon S3 for data persistence, utilizing IAM Least-Privilege Policies and S3 Presigned URLs to allow secure file downloads without exposing the bucket to the public internet.

💡 Engineering Highlights
Security-First Design: Implemented granular IAM roles for the Lambda "Brain," granting only the specific permissions needed to interact with the S3 bucket.

DevOps Workflow: Integrated a seamless local-to-cloud workflow where code changes are automatically packaged and deployed via the Terraform CLI.

Dynamic UX: Developed a responsive HTML/CSS dashboard that provides real-time status updates from the cloud environment.

🛠️ Deployment Instructions
Initialize: terraform init to download AWS providers.

Plan: terraform plan to review infrastructure changes.

Deploy: terraform apply -auto-approve to go live.

🚀 Why This Project Matters
By using Terraform, I’ve moved away from manual "click-ops" to a professional DevOps methodology. This approach allows a company to deploy this entire architecture across multiple global regions in seconds with perfect consistency.