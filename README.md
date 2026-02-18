🚀 **Live Demo:** ["https://3sxhm8etp1.execute-api.us-east-1.amazonaws.com/hello"]

🚀 Project Overview: Enterprise-Grade Serverless AI Intelligence Pipeline
This project architected a high-performance Event-Driven AI Microservice focused on automated document intelligence. By bridging Infrastructure-as-Code (IaC) with Generative AI, I engineered a secure, scalable solution that automates document processing—taking raw user uploads and delivering instant, AI-distilled insights through an asynchronous cloud pipeline.

🏗️ Engineering Highlights & Design Decisions
Infrastructure as Code (IaC): Orchestrated the entire AWS ecosystem (S3, Lambda, API Gateway, IAM) using Terraform. This ensures environment parity, eliminates manual configuration errors, and allows for rapid, reproducible deployments across staging and production.

Asynchronous Event-Driven Pipeline: Leveraged S3 Event Notifications to decouple storage from compute. This architectural pattern ensures the system scales elastically, triggering the Python-based Lambda "inference engine" the millisecond a new object is persisted.

LLM Integration (Generative AI): Integrated Amazon Bedrock (Anthropic Claude 3.5 Sonnet) to perform advanced Natural Language Processing. I optimized prompt engineering within the Lambda environment to ensure low-latency, high-accuracy summarization of unstructured text.

DevSecOps & Cloud Security: Strictly enforced the Principle of Least Privilege (PoLP) through fine-grained IAM policies. Enhanced data transit security by utilizing S3 Presigned URLs, mitigating the risks associated with public bucket access while maintaining a seamless user experience.