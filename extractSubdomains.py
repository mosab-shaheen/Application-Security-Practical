#!/user/bin/python
import sys
import re
def print_file(filename):
	f=open(filename, 'rU')
	lines=f.read()
	p = re.compile(r'(?:href|src)\s*=.*//(?:www\.)?((?:(?:[a-zA-Z0-9-]+)\.)+)(?:(?:[a-zA-Z0-9-]+)\.)[a-zA-Z]{2,4}') 
	t=p.findall(lines)
	subdomains=[x[:len(x)-1].lower() for x in t]#convert to lowercase and remove trailing dot
	print set(subdomains)
	f.close()
def main():
	print_file(sys.argv[1])
if __name__=='__main__':
	main()
