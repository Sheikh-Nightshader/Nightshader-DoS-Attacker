Nightshader DoS Attacker 1.0


A simple multi-protocol DoS testing tool made for **local pentesting only**.
Supports **HTTP**, **UDP**, and **TCP** attacks with threading, fake user-agents,
and Useful for testing how your own servers behave under load.

## Features
- HTTP flood with randomized user-agents
- UDP flood
- TCP flood
- Threaded attacks
- Color output (colorama)
- Simple banner (easy to replace with figlet)
- Pure Python (only `requests` needed for HTTP)

## Usage
Run the script:

    python3 dos.py

The tool will prompt you for:
- Attack type (HTTP / UDP / TCP)
- Target
- Port
- Number of threads

For HTTP, it rotates fake user-agents automatically.

## Requirements

    python3
    colorama
    requests   (optional, only for HTTP)

Install:

    pip install colorama requests

## Warning
This tool is **only for testing your own servers**.
Do **NOT** use it on systems you do not own or do not have permission to test.
You are fully responsible for using this tool ethically and legally!
