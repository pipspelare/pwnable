from pwn import p32, ssh, log

code_hash = 0x21DD09EC
num = code_hash // 5
remainder = code_hash % 5

buf = b""
buf += p32(num)
buf += p32(num)
buf += p32(num)
buf += p32(num)
buf += p32(num+remainder)

r = ssh('col', 'pwnable.kr', password='guest', port=2222)
p = r.process(executable='./col', argv=['col', buf])
flag = p.recv()

log.success(b"Flag: " + flag)
p.close()
r.close()
