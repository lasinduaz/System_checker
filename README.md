# System_checker

## Overview

System_checker is a simple Python script that provides a quick overview of your system's health, including operating system details, CPU usage, memory usage, and disk usage. It is useful for basic diagnostics and monitoring on Linux systems.

## Features

- Displays operating system and machine information
- Checks and reports CPU usage, with warnings for high usage
- Checks and reports memory usage, with warnings for high usage
- Checks and reports disk usage, with warnings for low disk space

## Requirements

- Python 3.6 or higher
- [psutil](https://pypi.org/project/psutil/) library

## Installation

1. Clone this repository or download the script.
2. (Recommended) Create and activate a virtual environment:
	```bash
	python3 -m venv env
	source env/bin/activate
	```
3. Install dependencies:
	```bash
	pip install psutil
	```

## Usage

Run the script using Python:

```bash
python check.py
```

You will see output for system information, CPU, memory, and disk status. Warnings are displayed if any resource usage is high.

## Example Output

```
=== SYSTEM INFORMATION ===
OS        : Linux
Machine   : x86_64

=== CPU STATUS ===
CPU Usage : 12.5%

=== MEMORY STATUS ===
Usage     : 45.3%

=== DISK STATUS ===
Usage     : 60.1%
```

## License

This project is licensed under the MIT License.