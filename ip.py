def generateIptables(ipList):
	ipListSplit=ipList.split("   ")
	output = open('data.txt', 'w')
	for i in range(0,len(ipListSplit)):
		ipt='iptables -I INPUT -s %s -j DROP' % ipListSplit[i]
		output.write(ipt)
		output.write('\n')
	output.close()

def main():
	generateIptables("23.23.197.123   162.242.157.195   200.19.191.98   176.32.85.11   109.123.85.149   54.204.42.168   213.171.6.8   54.251.40.61   94.73.160.194   85.24.176.2   218.26.12.1   219.143.74.43   178.162.193.132   94.127.136.76   54.246.219.212   200.239.65.43   143.205.180.163   183.60.156.48   50.97.138.102   219.140.194.146")

if __name__=="__main__":
	main()