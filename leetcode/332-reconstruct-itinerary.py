"""

332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the 
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when 
read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.


Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


INCOMPLETE

"""
from collections import defaultdict

class Solution(object):

	def dfs(self, graph, start, route, visited = None):
		if not visited: visited = set()
		print (start)

		visited.add(start)
		for dest in graph[start]:
			if dest not in visited:
				self.dfs(graph, dest, route, visited)
		
		

	"""
	:type tickets: List[List[str]]
	:rtype: List[str]
	"""
	def findItinerary(self, tickets):
		graph = defaultdict(list)
		visited = set()
		source = "JFK"
		route = []
		
		for src, dst in tickets:
			graph[src].append(dst)

		for src, dst in graph.items():
			dst.sort()
			print (src, dst)
	
		self.dfs(graph, source, route)
		return route
		


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]	
Solution().findItinerary(tickets)