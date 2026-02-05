# OmniSecure
🔐 OmniSecure – AI-Powered Security Monitoring Agent

OmniSecure is an AI-assisted endpoint security monitoring agent that observes system behavior in real time, detects suspicious activities, and uses an AI API (Scaledown) to analyze, correlate, and explain potential security threats.

Unlike traditional signature-based tools, OmniSecure focuses on behavioral analysis, anomaly detection, and AI-driven threat intelligence.

🚀 Key Features
🖥️ System Monitoring

CPU usage monitoring

Memory usage monitoring

Resource spike detection

🔍 Process Monitoring

Tracks running processes

Detects suspicious process names

Flags abnormal CPU consumption

📁 File Integrity Monitoring (FIM)

Detects file creation, modification, and deletion

Monitors critical directories

Forms the base for ransomware detection

🌐 Network Monitoring

Tracks active network connections

Detects unusual outbound ports

Identifies suspicious connection patterns

🤖 AI-Based Anomaly Detection

Uses Isolation Forest (unsupervised ML)

Learns normal system behavior

Detects deviations without signatures

🧠 AI-Assisted Threat Analysis (Scaledown API)

Correlates multiple security events

Assigns threat severity (Low → Critical)

Generates human-readable explanations

Suggests recommended actions

🧠 How OmniSecure Uses AI (Important)

AI is not used for raw monitoring.

Instead, OmniSecure:

Collects telemetry locally (safe & fast)

Detects suspicious behavior using rules + ML

Sends summarized events to the AI

AI provides:

Threat verdict

Reasoning

Recommended response

This design keeps:

✅ API costs low

✅ Privacy intact

✅ Decisions explainable

🏗️ Project Architecture
Endpoint Machine
│
├── Monitoring Layer
│   ├── System Monitor
│   ├── Process Monitor
│   ├── File Integrity Monitor
│   └── Network Monitor
│
├── AI & Logic Layer
│   ├── Anomaly Detector (ML)
│   ├── Threat Scoring Engine
│   ├── Event Correlation
│   └── AI Analyzer (Scaledown)
│
└── Logs & Intelligence
    ├── Local Logs
    └── AI Threat Explanations

📂 Project Structure
OmniSecure/
│
├── agent/
│   ├── main.py
│   ├── process_monitor.py
│   ├── file_monitor.py
│   ├── network_monitor.py
│   ├── anomaly_detector.py
│   ├── ai_analyzer.py
│   └── event_bus.py
│
├── logs/
│   └── events.log
│
├── watch_dir/
│
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/jekingsk/OmniSecure
cd omnisecure

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set AI API Key (Scaledown)
setx OMNISECURE_AI_KEY "your_scaledown_api_key"


Restart the terminal after setting the key.

▶️ Running OmniSecure

From the project root:

python agent/main.py


Logs will be written to:

logs/events.log

🧪 Example AI Threat Output
Threat Level: Critical

Reasoning:
The system shows abnormal file deletion activity combined with
high CPU usage by an unknown process and an outbound connection
to an uncommon port, indicating possible ransomware behavior.

Recommended Action:
Isolate the system and investigate the suspicious process immediately.

🔐 Ethical & Legal Notice

⚠️ OmniSecure must only be used on:

Systems you own

Authorized lab environments

Machines with explicit permission

❌ Do NOT use for:

Unauthorized surveillance

Credential harvesting

Privacy violations

🎯 Use Cases

AI-powered endpoint security prototype

Final-year / academic cybersecurity project

SOC & EDR concept demonstration

Behavioral malware research

AI + cybersecurity portfolio project

🚀 Future Enhancements

Real-time dashboard (SIEM-style UI)

MITRE ATT&CK mapping

Ransomware behavior classification

Cloud-based threat aggregation

Go-based high-performance agent

OmniSecure Project
AI-Driven Endpoint Threat Intelligence System
