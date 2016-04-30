"""
UBER Phone Interview
Design a structure that given a function callAPI()
restrict the number of calls per second to this function to 10

10 queries / second

Analysis:
    Current solution just handles batches of queries and executes the first 10
    and ignores all the other calls to the API *    

"""

# callAPI()
#   Restricted to 10 / second
# 

# Assuming we ignore calls after 10 happened

import time


class APIWrapper(object):
    def __init__(self):
        self.tasks = []
        self.maxTasks = 10
        
    def executeBatch(self, queries):
        for query in queries:
            self.executeCallAPI(
                query)

        self.run()
        
    def executeCallAPI(self, newTask):
        currTasks = len(self.tasks)
        if currTasks < self.maxTasks:
            self.tasks.append(newTask)
        

    
    def run(self):
        while self.tasks:
            task = self.tasks.pop()
            # callAPI()

second = 0
queries = []
wrapper = APIWrapper()

for i in range(100000):
    currTime = time.time()
    newSecond = int(currTime)
    
    if newSecond != second:        
        wrapper.executeBatch(queries)        
        queries = []
        second = newSecond
    else:
        queries.append(currTime)

print ("CALL", len(queries))
wrapper.executeBatch(queries)
    

    
    


