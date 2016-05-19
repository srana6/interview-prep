"""
Two Sigma engineers process large amounts of data every day, much more than any single server could possibly handle. 
Their solution is to user collections of servers, or server farms, to handle the massive computational load. 
Maintaining the server farms can get quite expensive, and because each server farm is simultaneously used by a number of 
different engineers, making sure that the servers handle their backlogs efficiently is critical.

Your goal is to optimally distribute a list of jobs between servers within the same farm. Since this problem cannot be solved in 
polynomial time, you want to implement an approximate solution using the Longest Processing Time (LPT) algorithm. This approach 
sorts the jobs by their associated processing times in descending order and then assigns them to the server that's going to become 
available next. If two operations have the same processing time the one with the smaller index is listed first. If there are several 
servers with the same availability time, then the algorithm assigns the job to the server with the smallest index.

Given a list of job processing times, determine how the LPT algorithm will distribute the jobs between the servers within the farm.

Example

For jobs = [15, 30, 15, 5, 10] and servers = 3, the output should be

serverFarm(jobs, servers) = [[1],
							 [0, 4],
							 [2, 3]]
job with index 1 goes to the server with index 0;
job with index 0 goes to server 1;
job with index 2 goes to server 2;
server 1 is going to be available next, since it got the job with the shortest processing time (15). Thus job 4 goes to server 1;
finally, job 3 goes to server 2.
[input] array.integer jobs

Unsorted array of positive integers representing the processing times of the given jobs.

[input] integer servers

A positive integer.

[output] array.array.integer

Array consisting of job indices grouped by which server they were run on. The ith row should contain 0-based indices of the jobs that were run on the ith server in the order of processing.

"""

from collections import deque

def serverFarm(jobs, servers):
	sortedJobs = []
	n = len(jobs)
	cum = 0
	groups = [[] for i in range(servers)]
	for i in range(n):
		sortedJobs.append((-jobs[i], i))
		cum += jobs[i]

	averageLoad = cum // servers
	sortedJobs.sort()
	sortedJobs = deque(sortedJobs)

	while sortedJobs:
		leastBusy = float("inf")
		leastIndex = 0
		for i in range(servers):
			cummulative = 0
			for index in groups[i]:
				cummulative += jobs[index]

			if leastBusy == cummulative:
				leastIndex = min(leastIndex, i)

			elif cummulative < leastBusy: 
				leastBusy = cummulative
				leastIndex = i

		job, index = sortedJobs.popleft()
		groups[leastIndex].append(index)

		return groups

	


"""
jobs = [15, 30, 15, 5, 10]
servers = 3

serverFarm(jobs, servers)


"""













"""
When visualizing market data over a long period of time, it is often helpful to build an Open-high-low-close (OHLC) chart. However, to build an OHLC chart you first need to prepare some data. For each financial instrument consider each day when it was traded, and find the following prices the instrument had that day:

open price: the price of the first trade of the day;
high price: the highest trade of the day;
low price: the lowest trade of the day;
close price: the price of the last trade of the day.
Given a stream of trade data ordered by time, write a program to compute the OHLC by day and instrument (see output section for the format details).

Example

For

timestamp = [1450625399, 1450625400, 1450625500, 
			 1450625550, 1451644200, 1451690100, 1451691000]
instrument = ["HPQ", "HPQ", "HPQ", "HPQ", "AAPL", "HPQ", "GOOG"],
side = ["sell", "buy", "buy", "sell", "buy", "buy", "buy"],
price = [10, 20.3, 35.5, 8.65, 20, 10, 100.35] and
size = [10, 1, 2, 3, 5, 1, 10], the output should be

dailyOHLC(timestamp, instrument, side, price, size) = 
[["2015-12-20", "HPQ", "10.00", "35.50", "8.65", "8.65"],
 ["2016-01-01", "AAPL", "20.00", "20.00", "20.00", "20.00"],
 ["2016-01-01", "GOOG", "100.35", "100.35", "100.35", "100.35"],
 ["2016-01-01", "HPQ", "10.00", "10.00", "10.00", "10.00"]]
[input] array.integer timestamp

A nondecreasing sequence of positive integers. timestamp[i] stands for the Unix time when the ith trade was made.

[input] array.string instrument

Array of the same length as timestamp. instrument[i] is the ticker symbol (identifier) for the financial instrument taking part in the ith trade.

[input] array.string side

Array of the same length as timestamp. side[i] equals either "buy" or "sell" depending on whether instrument[i] was bought or sold during the ith trade.

[input] array.float price

Array of the same length as timestamp. price[i] is the price of the instrument[i] during the ith trade. It is guaranteed that price[i] has no more than two digits after the decimal point.

[input] array.integer size

Array of the same length as timestamp. size[i] equals the number of shares of the instrument[i] traded during the ith trade.

[output] array.array.string

The ith row of the output should contain the following elements:

output[i][0] - date in the YYYY-MM-DD format;
output[i][1] - a ticker symbol for some instrument;
output[i][2] - a string corresponding to the open price;
output[i][3] - a string corresponding to the high price;
output[i][4] - a string corresponding to the low price;
output[i][5] - a string corresponding to the close price.
Each string corresponding to the price should contain exactly two digits after the decimal point and at least one digit before.

For each unique pair of a date and an instrument present in the inputs, such that there was a trade of that instrument on that day, there should be exactly one row in the output.

Output rows should be ordered by dates. Rows corresponding to the same date should be ordered in lexicographical order for ticker symbols.

"""

import datetime
def dailyOHLC(timestamp, instrument, side, price, size):
	dates = {}
	n = len(timestamp)
	result = []
	
	for i in range(n):
		day = datetime.datetime.fromtimestamp(timestamp[i]).strftime('%Y-%m-%d')
		dates[day] = dates.get(day, {})
		if instrument[i] not in dates[day]:
			dates[day][instrument[i]] = []
		dates[day][instrument[i]].append((side[i], price[i], size[i]))
		
	first = 0
	last = -1
	priceIndex = 1
	for day, companyList in dates.items():
		for company, transactionList in dates[day].items():
			initPrice = transactionList[first][priceIndex]
			openp, highp, lowp, closep = float(initPrice), float(initPrice), float(initPrice), float(transactionList[last][priceIndex])
			for i in range(1, len(transactionList)):
				c_side, c_price, c_size = transactionList[i]
				highp = max(highp, c_price)
				lowp = min(lowp, c_price)
				
			result.append([day, company, "%.2f" % openp, "%.2f" % highp, "%.2f" % lowp, "%.2f" % closep])
			
	result.sort()
	return result
			
			
			
			
"""            

timestamp = [1450625399, 1450625400, 1450625500, 
			 1450625550, 1451644200, 1451690100, 1451691000]
instrument = ["HPQ", "HPQ", "HPQ", "HPQ", "AAPL", "HPQ", "GOOG"]
side = ["sell", "buy", "buy", "sell", "buy", "buy", "buy"]
price = [10, 20.3, 35.5, 8.65, 20, 10, 100.35]
size = [10, 1, 2, 3, 5, 1, 10]

dailyOHLC(timestamp, instrument, side, price, size)

"""










from collections import deque
import copy 

def bfs(network, start, end, parent):
	visited = set()
	queue = deque([start])
	parent[start] = -1
	
	while queue:
		u = queue.popleft()
		for v, flow in enumerate(network[u]):
			if v not in visited and flow > 0:
				queue.append(v)
				parent[v] = u
				visited.add(v)
				
	return (end in visited)
	

def dataRoute(resource, server, network):
	start = resource
	end = server
	
	n = len(network)
	residual = copy.deepcopy(network)
	parent = [None] * n
	
	max_flow = 0
	while bfs(residual, start, end, parent): 
		path = float("inf")
		
		v = end
		while v != start:
			u = parent[v]
			path = min(path, residual[u][v])
			v = parent[v]
		
		v = end
		while v != start:
			u = parent[v]
			residual[u][v] -= path
			residual[v][u] += path
			v = parent[v]
			
		max_flow += path

	return max_flow
			
			
			
			

network = [[0, 2, 4, 8, 0, 0],
           [0, 0, 0, 9, 0, 0],
           [0, 0, 0, 0, 0, 10],
           [0, 0, 6, 0, 0, 10],
           [10, 10, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]


dataRoute(4, 5, network)