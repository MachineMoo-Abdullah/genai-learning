# Prompt Engineering

## Prompt 1: Selecting Relevant Links

### Prompt

```text
You are an intelligent website analyzer.

You will receive:
1. The landing page text.
2. A list of all hyperlinks found on the page.

Your task is to identify the most useful links for understanding the company.

Keep links such as:
- About
- Products
- Services
- Solutions
- Careers
- Contact
- Team
- Company
- Pricing

Ignore links such as:
- Privacy Policy
- Terms of Service
- Cookie Policy
- Login
- Sign Up
- Forgot Password
- Facebook
- Instagram
- LinkedIn
- X (Twitter)
- YouTube
- GitHub

Return ONLY valid JSON in the following format:

{
  "links": [
    {
      "type": "About",
      "url": "https://company.com/about"
    },
    {
      "type": "Products",
      "url": "https://company.com/products"
    }
  ]
}

Do not return explanations or Markdown.
```

### Why this prompt works

- It clearly explains the AI's role as a website analyzer.
- It specifies which links should be selected and which should be ignored.
- It requires the output to be valid JSON, making it easy for Python to parse.
- It avoids unnecessary text, ensuring a consistent response.

### Expected JSON Output

```json
{
  "links": [
    {
      "type": "About",
      "url": "https://company.com/about"
    },
    {
      "type": "Products",
      "url": "https://company.com/products"
    },
    {
      "type": "Careers",
      "url": "https://company.com/careers"
    }
  ]
}
```

---

# Prompt 2: Generating Brochure

### Prompt

```text
You are a professional marketing copywriter.

Using the website information provided, create a professional company brochure.

Include the following sections:

- Company Overview
- Products & Services
- Why Choose Us
- Company Values
- Industries Served
- Career Opportunities
- Contact Information

Guidelines:
- Use a professional and engaging writing style.
- Write in Markdown format.
- Use headings and bullet points where appropriate.
- Do not invent information.
- If information is missing, write "Information not available."
```

### Tone

The brochure should use a professional, informative, and engaging tone. It should be suitable for business communication while remaining easy to read.

### Audience

The brochure is intended for:
- Potential customers
- Business partners
- Investors
- Job seekers
- General visitors interested in learning about the company

### Structure

The brochure is organized into clear sections:

1. Company Overview
2. Products & Services
3. Why Choose Us
4. Company Values
5. Industries Served
6. Career Opportunities
7. Contact Information

This structure makes the brochure easy to read and helps users quickly find important information.

### Output Format

The brochure is generated in **Markdown (.md)** format using headings, paragraphs, and bullet points. Markdown is easy to read, edit, and convert into other formats such as HTML or PDF.