import random as r
tlb=[]
pagetable=[]
existpage=[]
exsitinst=[]
print('Implementation of TLB for a single process without Context Switching.\nIntructions:')
print('We consider only 1 process here.\nTime taken to access memory=100 micro secs.\nTime taken to access TLB is 20micro seconds.\nWe consider that each page has 50 instructions in it.')
print('We use Page size as 64')
n=8
timetlb=20
timemem=100
np=n*2
ni=32
time=0
print('Number of pages for the process=',np)
pagetable=[[x,r.randrange(100,800),-1] for x in range(np)]
print('\nPrinting Page Table:')
print('----------------------------------------')
for index,items,k in pagetable:
	print('Page No:',index,'\tFrame No:',items)
print('----------------------------------------')
print('Starting execution process:\n')

'''
for i in range(np):
	for j in range(ni):
		if (i,i+100) in tlb:
			time+=timetlb
			print('Page=',i,' presrent in TLB.(Hit)')
			time+=timemem
		else:
			time+=timetlb
			if len(tlb)==n:
				del(tlb[0])
				print('FIFO used to dump first inserted Page')
				print('\nUpdated TLB:')
				print('----------------------------------------')
				for index,items in tlb:
					print('Page No:',index,'\tFrame No:',items)
				print('----------------------------------------')
			tlb.append(pagetable[i])
			print('Page=',i,' not present in TLB, therefore added!(Miss)')
			print('\nUpdated TLB:')
			print('----------------------------------------')
			for index,items in tlb:
				print('Page No:',index,'\tFrame No:',items)
			print('----------------------------------------')
			time+=timemem
			time+=timemem



'''
while True:
	x=set([i[2] for i in pagetable])
	if len(x)==1 and 31 in x:
		break
	page=r.randrange(0,np)
	instruction=r.randrange(pagetable[page][2],32)
	if page in [x[0] for x in tlb]:
		time+=timetlb
		print('Page=',page,' present in TLB.(Hit)')
		time+=timemem
	else :
		time+=timetlb
		if len(tlb)==n:
			del(tlb[0])
			print('FIFO used to dump first inserted Page')
			print('\nUpdated TLB:')
			print('----------------------------------------')
			for index,items,k in tlb:
				print('Page No:',index,'\tFrame No:',items)
			print('----------------------------------------')
		tlb.append(pagetable[page])
		print('Page=',page,' not present in TLB, therefore added!(Miss)')
		print('\nUpdated TLB:')
		print('----------------------------------------')
		for index,items,k in tlb:
			print('Page No:',index,'\tFrame No:',items)
		print('----------------------------------------')
		time+=timemem
		time+=timemem	
	for i in range(instruction):
		if pagetable[page][2] == 31:
			break
		pagetable[page][2]+=1
	

avtime=time/(np*ni)
avtime_without_tbl=2*timemem
print('\n\nTotal time of execution for all instructions without TLB=',avtime_without_tbl*np*ni)
print('Average time of execution of an instruction without TLB=',avtime_without_tbl)
print('\n\nTotal time of execution for all instructions with TLB=',time)
print('Average time of execution of an instruction with TLB=',avtime)
