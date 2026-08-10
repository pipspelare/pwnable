from pwn import ssh

cafebabe = 0xcafebabe
seed = 1804289383

payload = cafebabe ^ seed

remote = ssh('random', 'pwnable.kr', password='guest', port=2222)
proc = remote.process(executable='./random')
print(f"\nattack with: {payload}\n")
proc.interactive()

remote.close()
