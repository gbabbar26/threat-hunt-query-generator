# What is this?

A Python-based AI tool designed for SOC analysts and threat hunters. Security professionals deal with an ever-evolving threat landscape — new vulnerabilities, new attack techniques, and new alerts daily. Instead of manually writing complex SIEM queries from scratch, analysts can simply describe the suspicious behaviour in plain English, specify their SIEM platform, and instantly get a ready-to-use query. Currently supports Splunk, Microsoft Sentinel, and Elastic.

## Why did I build this?

As a cybersecurity professional working on the defensive side, I deal with evolving threats daily. Writing precise SIEM queries from memory — or hunting through documentation every time — is time-consuming and pulls focus away from actual analysis. I built this tool to let AI handle the query syntax, so analysts can focus on what matters: investigating the threat. As I like to think of it — let AI do the hard part, so analysts can do the harder part.

## How it works:


Input Collection — Analyst describes the suspicious behaviour in plain English and specifies their SIEM platform (Splunk, Microsoft Sentinel, or Elastic)
AI Query Generation — The description is passed to Claude API with a threat hunting prompt, which generates a platform-specific, ready-to-use query
Error Handling — If query generation fails, the tool logs the error gracefully without crashing
Output — Generated query is displayed instantly in the terminal for immediate use

## How to run:
1. Clone the repository
   git clone https://github.com/gbabbar26/threat-hunt-query-generator.git

2. Install dependencies
   pip install anthropic

3. Set your API key
   Windows: set ANTHROPIC_API_KEY=your-key-here
   Mac/Linux: export ANTHROPIC_API_KEY=your-key-here

4. Run the tool
   python3 query_generator.py

5. Enter your threat description and SIEM platform when prompted
