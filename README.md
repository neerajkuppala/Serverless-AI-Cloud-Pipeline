🚀 **Live Demo:** [https://main.d2g1xi29ugsf8y.amplifyapp.com/]

🛠️ Backend API: https://3sxhm8etp1.execute-api.us-east-1.amazonaws.com/hello

# Serverless AI Text Summarizer 🚀

A full-stack, cloud-native application that leverages AWS serverless architecture to summarize long-form text and archive it in a NoSQL database.
![System Architecture](architecture.png)
## 🌟 Key Features
* **AI Summarization:** Processes raw text to generate concise, readable summaries.
* **Serverless Architecture:** Utilizes AWS Lambda for compute, ensuring high scalability and zero idle costs.
* **Persistent Storage:** Automatically archives every summary into Amazon DynamoDB with unique user-specific IDs.
* **Cloud Infrastructure:** Hosted and deployed via AWS Amplify for seamless CI/CD.

## 🏗️ Technical Architecture


1. **Frontend:** React/HTML/JS hosted on **AWS Amplify**.
2. **API Layer:** **Amazon API Gateway** manages RESTful communication and CORS headers.
3. **Compute:** **AWS Lambda (Python 3.11)** executes the backend logic and data processing.
4. **Database:** **Amazon DynamoDB** stores summaries using a schema optimized for high-cardinality lookups.

## 🛠️ Tech Stack
* **Language:** Python 3.11 (Backend), JavaScript (Frontend)
* **Cloud Provider:** AWS (Amplify, Lambda, DynamoDB, API Gateway, IAM, CloudWatch)
* **Infrastructure:** Boto3 (AWS SDK for Python)
* **Version Control:** Git & GitHub

## 🛡️ Challenges Overcame
* **Cross-Origin Resource Sharing (CORS):** Successfully implemented custom headers in Lambda and API Gateway to allow secure browser communication.
* **Infrastructure Mapping:** Debugged and resolved `ValidationExceptions` by aligning the Python data model with DynamoDB's Partition Key requirements.
* **Cloud Security:** Applied the **Principle of Least Privilege** using IAM policies to secure database write operations.

## 🚀 Future Roadmap
* Implement user authentication via **AWS Cognito**.
* Add a "History" dashboard to fetch and view past summaries using DynamoDB Query operations.
* Integrate Terraform for Infrastructure as Code (IaC) management.
