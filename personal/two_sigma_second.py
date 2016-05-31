"""
You are picking a series of optimum stocks for your investment portfolio. Thankfully, you have at your disposal a tool called ACME optimizer. For each stock it provides the expected future return in 1 year, as well as the expected risk during the same period. Your goal is to implement a stock picker which will maximize the sum of expected future returns while keeping the total risk under your risk budget (riskBudget).

Example

For stocks = [[-1, 2], [10, 15], [11, 13], [9, 10]] and riskBudget = 30, the output should be
optimalStockBasket(stocks, riskBudget) = 21.

It's a bad idea to pick the first stock because its expected future return is negative.
You can pick no more than two stocks from the remaining three because 15 + 13 + 10 > 30 (i.e. the total risk exceeds the risk budget if you pick all three of them). On the other hand, you can pick any pair of stocks because 15 + 13 ≤ 30, 15 + 10 ≤ 30, 13 + 10 ≤ 30.
To maximize the sum of expected future returns according to ACME optimizer predictions you need to pick the second and third stocks (1-based). The total future return in this case equals 10 + 11 = 21.
[input] array.array.integer stocks

stocks[i] consists of two integers: the first one corresponds to the expected future return of the ith stock in dollars, while the second one refers to the expected risk for the same stock.

It is guaranteed that stocks[i][1] > 0.

[input] integer riskBudget

A positive integer equal to the upper bound for the sum of the expected risks for the stocks which you can add to your portfolio.

[output] integer

The maximum possible sum of the expected future returns for the stocks you can add to your portfolio.

"""

def optimalStockBasket(stocks, riskBudget):
	n = len(stocks)
	returnIdx = 0
	riskIdx = 1
	
	memo = [[0] * (riskBudget + 1) for _ in range(n + 1)]
	
	for i in range(n + 1):
		for r in range(riskBudget + 1):
			if i == 0 or r == 0:
				memo[i][r] = 0
			
			elif stocks[i - 1][riskIdx] <= r and stocks[i - 1][returnIdx] >= 0:
				memo[i][r] = max(memo[i - 1][r], memo[i - 1][r - stocks[i - 1][riskIdx]] + stocks[i - 1][returnIdx])
			
			else:
				memo[i][r] = memo[i - 1][r]
	
	return memo[n][riskBudget]
	
	



	

"""

You know what they say: "time is money." In today's markets, the price of a stock that you see on your computer might not be the price that you end-up trading at, since by the time your request reaches the exchange the price might have changed. Therefore, the quicker you can get your order to the exchange, the better the chances that you will trade at your expected price.

Picture a peer-to-peer computer network of n nodes that's supposed to route your request from your computer to a computer where the trade is actually registered. Let's assume that the network is not optimized yet, so it's your task to implement an algorithm that computes the shortest path from the source at index 1 (your computer) to the destination at index n.

Example

For n = 4 and

network = [[1, 4, 200], 
           [1, 2, 5], 
           [1, 3, 10], 
           [2, 3, 4], 
           [2, 4, 150], 
           [3, 4, 100]]
the output should be
computerNetwork(n, network) = 109.

The shortest path is 1 -> 2 -> 3 -> 4.



[input] integer n

A positive integer equal to the number of nodes in the network.

[input] array.array.integer network

For each valid i, network[i] consists of three positive integers and corresponds to the two-way connection between the nodes network[i][0] and network[i][1]. Routing the stock order through that connection takes network[i][2] milliseconds.

It is guaranteed that there is a route between any pair of nodes. It is also guaranteed that there is no more than one direct connection between any pair of nodes.

1 ≤ network[i][0], network[i][1] ≤ n
network[i][2] > 0

[output] integer

The minimum time needed to route the stock from node 1 to node n in milliseconds.

"""

import heapq

MAX = float("inf")

def computerNetwork(n, network):
	graph = [[0] * n for _ in range(n)]
	for u, v, w in network:
		graph[u - 1][v - 1] = w
		graph[v - 1][u - 1] = w
	
	src = 0
	dest = n - 1
	
	distance = [MAX] * n
	distance[src] = 0
	visited = set()
	queue = [(0, src)]
	
	while queue:
		value, node = heapq.heappop(queue)
		visited.add(node)
		
		for adj, w in enumerate(graph[node]):
			if adj not in visited and w > 0:
				if distance[adj] > distance[node] + w:
					distance[adj] = distance[node] + w
					heapq.heappush(queue, (distance[adj], adj))
	
	return distance[dest]











import heapq

def jobScheduling(requestTime, jobProcess, timeFromStart):
  n = len(jobProcess)
  currTime = 0
  i = 0
  work = 0
  queue = []
  
  while currTime <= timeFromStart:
    print (currTime, queue, work)
    while i < n and currTime == requestTime[i]:
        heapq.heappush(queue, (jobProcess[i], i))
        i += 1
    
    print (currTime, queue)
    # Show current time before removing next Job
    if currTime == timeFromStart:
      break
    
    if work <= 0 and queue:
      workLoad, ith = heapq.heappop(queue)
      work = workLoad
          
    work -= 1
    currTime += 1
  
  queue.sort()
  result = []
  for job, index in queue:
    result.append(index)
    
  return result




"""




class Pair implements Comparable<Pair> {
  public int index;
  public int value;
  
  public Pair(int index, int value){
    this.index = index;
    this.value = value;
  }
  
  @Override
  public int compareTo(Pair other){
    return Integer.valueOf(value).compareTo(other.value);
  }
}

int[] resultToArray(PriorityQueue<Pair> queue){
  int[] result = new int[queue.size()];
  Iterator<Pair> iter = queue.iterator();
  
  int i = 0;
  while(!queue.isEmpty()){
    Pair job = queue.poll();
    result[i] = job.index;
    i++;
  }
  
  return result;
}

int[] jobScheduling(int[] requestTime, int[] jobProcess, int timeFromStart) {
  PriorityQueue<Pair> queue = new PriorityQueue<Pair>();
  ArrayList<Integer> result = new ArrayList<>();
  int n = jobProcess.length;
  int i = 0;
  int work = 0;
  int currTime = 0;
  
  while (currTime <= timeFromStart){
    while (i < n && currTime == requestTime[i]){
      queue.add(new Pair(i, jobProcess[i]));
      i++;
    }
    
    if (currTime == timeFromStart){
      break;
    }
    
    if (work <= 0 && !queue.isEmpty()){
      Pair job = queue.poll();
      work = job.value;
    }
    
    work --;
    currTime ++;
  }
  
  return resultToArray(queue);
}


"""