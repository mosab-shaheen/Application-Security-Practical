#!/user/bin/python
def pattern_sum(k,m):
	if (k<1) or (k>9) or (m<1) or (m>9):
		print 'Error: Check Values'
	else:
		sum=0
		for i in range(1,m+1):
			temp=0
			for j in range(1,i+1):
				print k,
				temp=temp*10+k
			if i != m:
				print ' + ',
			sum=sum+temp
	return sum
def main():
	try:
		kStr= raw_input('Enter k=')
		mStr= raw_input('Enter m=')
		k= int(kStr)
		m= int(mStr)
		sum = pattern_sum(k,m)
		print '\n'
		print 'sum=', sum
	except:
		print 'Error Happend'
if __name__=='__main__':
	main()

