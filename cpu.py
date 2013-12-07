import sys

memory = [0]*32778
stack = []
ip = 0

def loadmem():
	ifile = sys.stdin.read()
	i = 0
	j = 0
	while j<len(ifile): 
		memory[i] = ord(ifile[j]) | (ord(ifile[j+1])*256)
		j+=2
		i+=1

loadmem()

while 1:
	inst = memory[ip]
	#print memory[32767:32778]
	a, b, c = memory[ip+1],memory[ip+2],memory[ip+3]
	#print "\rip:",ip,
	#print "i:", inst,"a,b,c:",a,b,c
	#print "\r", stack,
	if inst==0: 
		break
	elif inst==1:
		#print "set register", a, "to", b
		if b>32767: memory[a] = memory[b]
		else: memory[a] = b
		ip+=3
	elif inst==2:
		#print "push",a,"onto the stack"
		if a>32767: a=memory[a]
		stack.append(a)
		ip+=2
	elif inst==3:
		#print "pop from the stack into",a
		memory[a] = stack.pop()
		ip+=2
	elif inst==4:
		#print "set",a, "to 1 if", b,"==",c,"else set it to 0"
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		if b == c: memory[a] = 1
		else: memory[a] = 0
		ip+=4
	elif inst==5:
		#print "set",a, "to 1 if", b,">",c,"else set it to 0"
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		if b > c: memory[a] = 1
		else: memory[a] = 0
		ip+=4
	elif inst==6:
		#print "jump to", a
		ip = a
	elif inst==7:
		#print "if",a,"nonzero, jump to",b
		jumped = 0
		if 0 < a and (a < 32768 or memory[a]): ip = b
		else: ip+=3
	elif inst==8:
		#print "if",a,"zero, jump to",b
		if a == 0 or (a>32767 and memory[a] == 0): ip = b
		else: ip+=3
	elif inst==9:
		#print "assign into",a,"the sum of", b,"and",c
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		memory[a] = (b+c)%32768
		ip+=4
	elif inst==10:
		#print "assign into",a,"the product of", b,"and",c
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		memory[a] = (b*c)%32768
		ip+=4
	elif inst==11:
		#print "assign into",a,"the remainder of", b,"/",c
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		memory[a] = (b%c)%32768
		ip+=4
	elif inst==12:
		#print "assign into",a,"the bitwise AND of", b,"and",c
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		memory[a] = (b&c)%32768
		ip+=4
	elif inst==13:
		#print "assign into",a,"the bitwise OR of", b,"and",c
		if b>32767: b=memory[b]
		if c>32767: c=memory[c]
		memory[a] = (b|c)%32768
		ip+=4
	elif inst==14:
		#print "assign into",a,"the bitwise NOT of", b
		if b>32767: b=memory[b]
		memory[a] = (~b)%32768
		ip+=3
	elif inst==15:
		#print "read memory value", b, "into",a
		if b>32767: b=memory[b]
		memory[a] = memory[b]
		ip+=3
	elif inst==16:
		#print "write", b, "to memory value",a
		if a>32767: a=memory[a]
		if b>32767: b=memory[b]
		memory[a] = b
		ip+=3
	elif inst==17:
		#print "call",a
		if a>32767: a=memory[a]
		stack.append(ip+2)
		ip = a
	elif inst==18:
		d = stack.pop()
		#print "returning to",d
		ip = d
	elif inst==19:
		if a>32767: a=memory[a]
		sys.stdout.write(chr(a))
		ip+=2
	elif inst==20: 
		memory[a] = sys.stdin.read(1)
		ip+= 2
	elif inst==21: 
		#print "no op"
		ip+= 1
	else:
		print "Unrecognized instruction",inst
		break

print "Halted"