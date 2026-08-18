from pwn import ssh

executeable = "nc 0 10010"

remote = ssh('blackjack', 'pwnable.kr', password='guest', port=2222)
proc = remote.run(['bash', '-c', executeable])
print("\n Bet -1000000 dollars and lose intentionally \n")
proc.interactive()
