1. Zero-shot Prompting
- Prompt: Summarize the following paragraph in five sentences:
Artificial Intelligence is transforming healthcare by assisting doctors with diagnosis, improving medical imaging, predicting diseases, and automating administrative tasks. AI systems analyze large amounts of patient data to identify patterns that help in making better medical decisions.

- Response: Here is a five-sentence summary:
Artificial Intelligence is changing healthcare by helping doctors diagnose diseases more accurately. It improves medical imaging and helps predict diseases before they become serious. AI analyzes large amounts of patient data to identify useful patterns. These patterns support doctors in making better medical decisions. AI also automates administrative tasks, making healthcare more efficient.

- Prompt: Translate the following sentence into French:
Machine learning helps computers learn from data without being explicitly programmed.

- Response: French translation:
L'apprentissage automatique permet aux ordinateurs d'apprendre à partir de données sans être explicitement programmés.

- Prompt: Explain the concept of Cloud Computing in simple words for a beginner.

- Response: Cloud computing means using computers, storage, and software over the internet instead of on your own computer.
Imagine you have photos on your phone. Instead of saving them only on your phone, you save them to Google Drive or iCloud. You can then access those photos from any device with an internet connection. This is an example of cloud computing.

Simple Definition
Cloud computing is the delivery of computing services—such as storage, servers, databases, networking, and software—over the internet ("the cloud").

Example
Instead of installing Microsoft Office on your computer, you use Google Docs in your web browser. The software and your files are stored on remote servers, not on your computer.

Advantages
Access your data from anywhere with an internet connection.
Save money because you don't need expensive hardware.
Easily increase or decrease resources as needed.
Data is often backed up automatically.
Easy to share files and collaborate with others.
Popular Cloud Services
Google Drive
Dropbox
Microsoft OneDrive
Amazon Web Services (AWS)
Microsoft Azure
Google Cloud Platform (GCP)

In simple terms, cloud computing is like renting computing resources over the internet instead of buying and maintaining them yourself.

2. One-shot Prompting
- Prompt: Example:
Text: I absolutely love this laptop. It is fast and reliable.
Sentiment: Positive

Now classify the following:
Text: The phone battery drains very quickly and the camera quality is poor.
Sentiment:

- Response: 
Sentiment: Negative

The text expresses dissatisfaction with the phone because it mentions two negative aspects:

The battery drains very quickly.
The camera quality is poor.

Therefore, the overall sentiment is Negative.

-Prompt: Example:
Input: Apple
Category: Fruit

Now classify:

Input: Carrot
Category:

- Response: 
Category: Vegetable

- Prompt: Example:
Situation: Employee is sick.

Email:
Dear Manager,
I am feeling unwell today and would like to request one day of leave. I will resume work tomorrow.
Thank you.

Now write an email for:
Situation: Employee requests leave to attend a family wedding.

- Response: Dear Manager,

I hope you are doing well.

I would like to request leave to attend a family wedding. The event is important to my family, and my presence is required. I will ensure that my current work is completed or properly handed over before my leave.

Thank you for your understanding. I look forward to your approval.

Kind regards,
[Your Name]

3. Few-shot Prompting
- Prompt: Examples:

Dog → Animal
Rose → Flower
Eagle → Bird
Lion → Animal

Now classify:

Shark →

- Response:
Shark → Fish

- Prompt:
Examples:
Good Morning → Bonjour
Thank You → Merci
Good Night → Bonne Nuit

Translate:
See you tomorrow →
- Response:
See you tomorrow → À demain

- Prompt:
Examples:
print("Hello") → Python

System.out.println("Hello"); → Java

cout << "Hello"; → C++

Now identify:

console.log("Hello");

- Response:
Answer: JavaScript
console.log("Hello"); is the standard syntax in JavaScript for printing output to the console.

4. Persona Prompting:

- Prompt:
You are a Senior Software Engineer.

Explain the advantages and disadvantages of Microservices Architecture for a large e-commerce application.
- Response:
As a Senior Software Engineer, here's a balanced explanation of Microservices Architecture for a large e-commerce application.

What is Microservices Architecture?

Microservices architecture is a software design approach where a large application is divided into small, independent services. Each service is responsible for a specific business function and communicates with other services through APIs.

For an e-commerce application, services might include:

User Service
Product Catalog Service
Shopping Cart Service
Order Service
Payment Service
Inventory Service
Notification Service

Each service can be developed, deployed, and scaled independently.

Advantages
1. Independent Scalability

Different services can be scaled based on demand.

Example:
During a sale, only the Product Catalog and Order services may need extra servers, while the User Service remains unchanged.

2. Faster Development

Multiple teams can work on different services simultaneously without interfering with each other.

3. Independent Deployment

A single service can be updated without redeploying the entire application.

Example:
Updating the Payment Service does not require restarting the Product Catalog.

4. Fault Isolation

If one service fails, the rest of the application can often continue operating.

Example:
If the Notification Service is down, customers can still place orders.

5. Technology Flexibility

Each service can use the technology best suited to its purpose.

Example:

Product Search → Elasticsearch
Payment → Java
Recommendation Engine → Python
Frontend APIs → Node.js
6. Easier Maintenance

Smaller codebases are generally easier to understand, test, and maintain than one large application.

7. Better CI/CD Support

Independent services fit well with continuous integration and continuous deployment pipelines, enabling frequent releases.

Disadvantages
1. Increased Complexity

Managing many services is more complex than managing a single application.

Developers must handle:

Service discovery
API gateways
Configuration management
Monitoring
Logging
2. Network Communication Overhead

Services communicate over the network instead of calling methods directly, introducing additional latency and possible communication failures.

3. Distributed Data Management

Each service often owns its own database, making transactions across services more difficult.

Example:
Creating an order may require updates to the Order, Payment, and Inventory services while maintaining consistency.

4. Harder Testing

End-to-end testing becomes more challenging because multiple services interact with each other.

5. Deployment and Infrastructure Cost

Microservices often require:

Containers (Docker)
Orchestration (Kubernetes)
Load balancers
Monitoring tools
API gateways

These increase operational complexity and cost.

6. Monitoring and Debugging

Tracing a request across multiple services requires distributed tracing and centralized logging.

Common tools include:

Jaeger
Zipkin
Prometheus
Grafana
ELK Stack
7. Security Challenges

More APIs and service-to-service communication create a larger attack surface. Authentication, authorization, and encryption must be managed carefully.

- Prompt:
You are an experienced HR Manager.
Write five interview questions for a Machine Learning Engineer position.

- Response:
As an experienced HR Manager, here are five interview questions for a Machine Learning Engineer position:

1. Can you briefly introduce yourself and describe your experience with machine learning projects?

   Purpose: Understand the candidate's background, communication skills, and relevant experience.

2. Tell me about a challenging machine learning project you worked on. What was your role, and how did you overcome the challenges?

   Purpose: Evaluate problem-solving ability, technical involvement, and teamwork.

3. How do you stay updated with the latest developments in machine learning and artificial intelligence?

   Purpose: Assess the candidate's commitment to continuous learning and professional growth.

4. Describe a situation where you had to explain a complex machine learning concept to someone without a technical background. How did you approach it?

   Purpose: Measure communication skills and the ability to simplify technical concepts for stakeholders.

5. Why do you want to join our company as a Machine Learning Engineer, and what value do you believe you can bring to our team?

   Purpose: Understand motivation, cultural fit, and how the candidate aligns with the organization's goals.

- Prompt:
You are a Cybersecurity Expert.
Explain how phishing attacks work and provide five ways to prevent them.

- Response:
As a **Cybersecurity Expert**, here's a beginner-friendly explanation.

## What is a Phishing Attack?

A **phishing attack** is a type of cyberattack in which an attacker pretends to be a trusted person or organization to trick victims into revealing sensitive information such as passwords, credit card numbers, bank details, or personal information.

Phishing attacks are commonly delivered through:

* Emails
* SMS messages (Smishing)
* Phone calls (Vishing)
* Fake websites
* Social media messages

## How Phishing Attacks Work

1. **The attacker creates a fake message**

   * The message appears to come from a trusted source such as a bank, online store, or company.

2. **The victim receives the message**

   * The message often creates urgency, for example:

     * "Your account has been suspended."
     * "Verify your identity immediately."
     * "You've won a prize."

3. **The victim clicks a malicious link or opens an attachment**

   * The link leads to a fake website that closely resembles the legitimate one, or the attachment installs malware.

4. **The victim enters sensitive information**

   * Thinking the site is genuine, the victim enters usernames, passwords, or payment details.

5. **The attacker steals the information**

   * The stolen credentials may be used to access accounts, steal money, commit identity theft, or launch additional attacks.

## Five Ways to Prevent Phishing Attacks

1. **Verify the sender**

   * Check the sender's email address or phone number carefully. Be cautious of slight misspellings or unusual domains.

2. **Avoid clicking suspicious links**

   * Hover over links to preview their destination before clicking. If unsure, type the official website address directly into your browser.

3. **Enable Multi-Factor Authentication (MFA)**

   * MFA adds an extra layer of security, making it harder for attackers to access your accounts even if they obtain your password.

4. **Keep software updated**

   * Regularly update your operating system, browser, antivirus software, and applications to protect against known vulnerabilities.

5. **Be cautious with urgent or unexpected requests**

   * Treat messages requesting passwords, financial information, or immediate action with skepticism. Verify such requests through official channels before responding.

## Example

You receive an email claiming to be from your bank saying:

> "Your account will be locked in 24 hours. Click here to verify your account."

The link directs you to a website that looks like your bank's login page. After entering your username and password, the information is sent to the attacker instead of the bank. The attacker can then use your credentials to access your real account.

## Conclusion

Phishing attacks rely on **deception and social engineering** rather than technical hacking. Staying alert, verifying requests, using strong security practices like MFA, and avoiding suspicious links are among the most effective ways to protect yourself and your organization.

5. Structured Output:

- Prompt:
Generate the following information in JSON format:
Name: Ali Khan
Age: 22
Department: Artificial Intelligence
Skills: Python, SQL, Machine Learning
Experience: Internship at XYZ Company

- Response:
{
  "name": "Ali Khan",
  "age": 22,
  "department": "Artificial Intelligence",
  "skills": [
    "Python",
    "SQL",
    "Machine Learning"
  ],
  "experience": {
    "position": "Intern",
    "company": "XYZ Company"
  }
}

- Prompt:
Create a Markdown table comparing Python, Java, and C++ based on:

- Difficulty
- Speed
- Common Uses
- Learning Curve

- Response:
| Feature            | Python                                                      | Java                                                          | C++                                                                                   |
| ------------------ | ----------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Difficulty**     | Easy                                                        | Moderate                                                      | Hard                                                                                  |
| **Speed**          | Slower                                                      | Fast                                                          | Very Fast                                                                             |
| **Common Uses**    | Data Science, AI/ML, Web Development, Automation, Scripting | Enterprise Applications, Android Development, Backend Systems | Game Development, System Programming, Embedded Systems, High-Performance Applications |
| **Learning Curve** | Beginner-friendly                                           | Moderate                                                      | Steep                                                                                 |

- Prompt:
Generate CSV data for five students containing:

Student ID
Name
Department
CGPA

- Response:
Student ID,Name,Department,CGPA
101,Ali Khan,Artificial Intelligence,3.82
102,Sara Ahmed,Computer Science,3.76
103,Hassan Raza,Software Engineering,3.91
104,Ayesha Malik,Data Science,3.68
105,Umar Farooq,Cybersecurity,3.85

6. Chain Prompting:
- Prompt:
Summarize the following article in five bullet points.https://www.nature.com/subjects/machine-learning

- Response:
Here is a five-bullet summary of the Nature Machine Learning topic page:

* Machine learning is a branch of artificial intelligence that enables computers to learn from data and improve their performance without being explicitly programmed. It is widely used in areas such as data mining, healthcare, biology, and scientific research. ([Nature][1])
* Recent research highlights the growing use of AI and large language models in medicine, including disease diagnosis, medical imaging, protein analysis, and automated clinical reporting.
* Machine learning is driving advances in biomedical research, helping scientists generate hypotheses, predict disease risks, discover drug candidates, and analyze complex biological data more efficiently. 
* Nature also features articles discussing the broader impact of AI, including cybersecurity, AI safety, scientific discovery, gene regulation, and CRISPR-based biotechnology. 
* The page is regularly updated with research papers, reviews, news, and expert commentary, making it a valuable resource for keeping up with the latest developments in machine learning.

- Prompt:
Using the summary you created, identify the three most important findings.

- Response:
Based on the summary, the three most important findings are:

1. Machine learning enables computers to learn from data and make intelligent decisions. It is a core technology behind modern AI and is widely used in healthcare, finance, biology, and scientific research.

2. Machine learning is transforming healthcare and biomedical research. It helps with disease diagnosis, medical imaging, drug discovery, protein analysis, and clinical decision-making.

3. Machine learning is accelerating scientific innovation. AI technologies, including large language models, help researchers analyze complex data, automate workflows, and solve challenging scientific problems.

- Prompt:
Using those findings, create a PowerPoint presentation outline with:

- Title Slide
- Introduction
- Main Findings
- Conclusion

- Response:
# PowerPoint Presentation Outline

## Slide 1: Title Slide

* Title: Machine Learning: Key Findings and Applications
* Subtitle: An Overview of Recent Developments
* Presenter: [Your Name]
* Date: [Presentation Date]

---

## Slide 2: Introduction

* What is Machine Learning?
* Importance of machine learning in today's world
* Growing impact across industries such as healthcare, finance, and scientific research

---

## Slide 3: Main Findings

### Finding 1

* Machine learning enables computers to learn from data and make intelligent decisions.
* It is widely used in healthcare, finance, biology, and scientific research.

### Finding 2

* Machine learning is transforming healthcare and biomedical research.
* It supports disease diagnosis, medical imaging, drug discovery, protein analysis, and clinical decision-making.

### Finding 3

* Machine learning is accelerating scientific innovation.
* AI technologies help researchers analyze complex data, automate workflows, and solve challenging scientific problems.

---

## Slide 4: Conclusion

* Machine learning is a key technology driving innovation across multiple fields.
* Its applications continue to improve healthcare, research, and decision-making.
* As AI advances, machine learning will play an even greater role in solving real-world problems.
