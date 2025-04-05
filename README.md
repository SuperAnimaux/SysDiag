## Preamble  
This tool is designed to bring together in one place the necessary functionalities for diagnosing a computer running Windows as its operating system. This project is still in its early stages, is under development, and will continue to evolve. **This tool does not support automatic diagnostics; it simply provides information to facilitate diagnostics.**

## Current Features
* General information about the CPU
* General information about the GPU
* General information about the RAM
* General information about storage
* Visualization of storage usage (HDD/SSD)
* Windows update check
* Listing of Windows logs
* Verification of Windows log integrity (admin)

## Modules used

* **evtx**, version : 0.8.9
* **pywin32**, version : 308
* **psutil**, version : 6.1.1

## Installation  

Copy this project to your computer:

```bash
git clone https://github.com/SuperAnimaux/SysDiag.git
```

Install the requirements

```bash
pip install -r requirements.txt
```

Run main.py:

```bash
python main.py
```

**The installation of Python and some additional modules is required.**
