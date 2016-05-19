"""
Yelp Technical Interview


United States ->
California -> 
San Francisco -> 
Golden Gate Bridge


United States 
    California
        San Francisco        
    Florida    

"""

from collections import deque

# Given Wikipedia Pages are defined as:
class WikipediaPage(object):
    def __init__(self, other_pages=[]):
        self.other_pages = other_pages 
        
# and a start WikipediaPage (start_page) and a destination WikipediaPage
# (destination_page), find the fewest number of links that needed to be
# clicked to get from the start to the destination.

def find_fewest_clicks(start_page, destination_page):
    distance = {}
    distance[start_page] = 0
    visited = set()
    queue = deque([start_page])
    
    while queue:
        node = queue.popleft()
        visited.add(node)
        n = len(node.other_pages)
        
        if node == destination_page:
            return distance[distination_page]
        
        for u in range(n):
            adjacent = node.other_pages[u]
            if adjacent not in visited:
                queue.append(adjacent)
                distance[adjacent] = min(distance[adjacent], distance[node] + 1) # :)
                
    return 0