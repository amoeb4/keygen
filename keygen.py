import os

key = os.urandom(16)
print(f"generated key = {key.hex()}")

iv = os.urandom(16)
print(f"generated key = {iv.hex()}")

new = iv + key
print(f"{new.hex()}")

sys = key + iv
print(f"{sys.hex()}")

kard = iv 
