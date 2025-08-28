# Layout Parser CLI Tool

A lightweight command-line tool to parse simplified GDSII-like layout files and extract DRC/LVS violations using rule-based logic.

## 🔧 Features
- Parses layout blocks from text input
- Applies spacing and enclosure rules from a YAML rule deck
- Logs violations with coordinates and rule IDs
- Designed for educational and pre-signoff layout validation

## 🧪 Tech Stack
Python, Bash, Regex, YAML, TCL (basic)

## 🚀 Usage
```bash
python parser.py layout.txt rules.yaml
