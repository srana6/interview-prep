import re
from collections import deque
regex = re.compile('[^a-z]')

def jaccard(word1, word2):
    index = 0
    intersection = float(len(word1.intersection(word2)))
    union = float(len(word1.union(word2)))            
    if intersection == 0 and union == 0:
        index = 1
    else:
        index = intersection / union
    return index

class Cluster(object):
    def __init__(self, elem, word):
        self.elem = [elem]
        self.words = [word]
        self.size = 1
    
    def merge(self, other):
        print (self.elem , other.elem)
        self.elem = self.elem + other.elem
        self.words = self.words + other.words
        self.size = len(self.elem)
        
    def similarity(self, other, threshold):
        similar = False
        
        max_jaccard = 0
        this_words = self.words
        other_words = other.words
        
        for i in range(len(this_words)):
            for j in range(len(other_words)):
                max_jaccard = max(max_jaccard, jaccard(this_words[i], other_words[j]))
                
        if max_jaccard >= threshold:
            similar = True
            
        return similar

def get_clusters(words, threshold):
    clusters = deque([])
    n = len(words)
    for i in range(n):
        new_cluster = Cluster(i, words[i])        
        clusters.append(new_cluster)

    changes = n
    while changes > 0:
        curr_cluster = clusters.popleft()
        
        cluster_size = len(clusters)
        for c in reversed(range(cluster_size)):
            if curr_cluster.similarity(clusters[c], threshold):
                curr_cluster.merge(clusters[c])            
                changes += 1
                del clusters[c]
        
        clusters.append(curr_cluster)
        changes -= 1
    return clusters  



"""
class Cluster(object):
    def __init__(self,indexes, words):
        self.indexes = indexes
        self.words = words
        self.size = len(indexes)
    
    def merge(self, other):
        self.indexes = self.indexes + other.indexes
        self.words = self.words.union(other.words)
        self.size = len(self.indexes)

def get_clusters(words, threshold):
    clusters = deque([])
    n = len(words)
    for i in range(n):
        new_cluster = Cluster([i], words[i])        
        clusters.append(new_cluster)

    changes = n
    while changes > 0:
        curr_cluster = clusters.popleft()
        
        cluster_size = len(clusters)
        for c in reversed(range(cluster_size)):
            intersection = float(len(curr_cluster.words.intersection(clusters[c].words)))
            union = float(len(curr_cluster.words.union(clusters[c].words)))            
            if intersection == 0 and union == 0:
                index = 1
            else:
                index = intersection / union
            
            if index >= threshold:
                changes += 1
                curr_cluster.merge(clusters[c])
                del clusters[c]
        
        clusters.append(curr_cluster)
        changes -= 1
    return clusters  


"""

def spamClusterization(requests, IDs, threshold):
    if not requests or not IDs or len(IDs) != len(requests): return []
    if threshold < 0 or threshold > 1: return []
    
    n = len(requests)
    jaccard = [([None] * n) for _ in range(n)]
    words = []
    for request in requests:
        new_set = set()
        for word in request.split():
            _word = regex.sub('', word.lower())
            if _word:
                new_set.add(_word)
        words.append(new_set)
                
    clusters = get_clusters(words, threshold)    
    result = []
    
    for cluster in clusters:
        if cluster.size > 1:
            valid_cluster = []
            for elem in cluster.elem:
                print (elem)
                valid_cluster.append(IDs[elem])
            valid_cluster.sort()
            result.append(valid_cluster)
    result.sort()
    print (result)
    return result
            



requests =  ["I need a new window.", 
 "I really, really want to replace my window!", 
 "Replace my window.", 
 "I want a new window.", 
 "I want a new carpet, I want a new carpet, I want a new carpet.", 
 "Replace my carpet"]
IDs = [374, 2845, 83, 1848, 1837, 1500]
threshold = 0.5

spamClusterization(requests, IDs, threshold)