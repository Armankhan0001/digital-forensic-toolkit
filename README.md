🛡️ Digital Forensics Toolkit

A lightweight Command-Line Digital Forensics Toolkit built in Python for analyzing files, detecting steganography, calculating hashes, extracting metadata, and monitoring directories in real time.

Designed for cybersecurity students, DFIR beginners, and Linux-based forensic analysis (tested on Kali Linux).

🚀 Features

🔍 Steganography Detection (LSB-based analysis)

🔐 Hash Generation (MD5, SHA1, SHA256)

🧾 Metadata Extraction (Images & Files)

📁 Real-time Directory Monitoring

📊 JSON-based structured forensic output

🐍 Fully Python-based and lightweight

🛠️ Requirements

Python 3.8+

Kali Linux / Linux OS recommended

Install dependencies:

pip3 install pillow watchdog
📂 Project Structure
Digital-Forensics-Toolkit/
│
├── main.py
├── modules/
│   ├── stego.py
│   ├── hashcalc.py
│   ├── metadata.py
│   └── watcher.py
└── README.md
▶️ How to Run

Navigate to project directory:

cd /home/kali/Digital-Forensics-Toolkit
🔍 Steganography Detection
python3 main.py stego test.jpg
🔐 Generate File Hashes
python3 main.py hash test.jpg
🧾 Extract Metadata
python3 main.py meta test.jpg
📁 Monitor Directory (Real-Time)
python3 main.py watch /home/kali/Downloads
📌 Example Output
{
    "file": "test.jpg",
    "stego_detected": false,
    "entropy": 4.87,
    "lsb_score": 0.14
}
🎯 Use Cases

Cybercrime investigation basics

Digital evidence validation

Academic cybersecurity projects

Portfolio project for DFIR roles

Learning file analysis techniques

⚠️ Disclaimer

This tool is developed for educational and defensive cybersecurity purposes only. The author is not responsible for misuse.

Cybersecurity & Digital Forensics Enthusiast
