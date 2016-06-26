"""
Time   O(n lg n)
Space  O(n)

In order to keep track of fraudulent transactions and remember its ordering, an ordered dictionary its very helpful due to it works as a hashmap (for the names) while remembering the order of insertion,
however, there are particular cases when a fraud is detected after several normal transactions. For this reason, its required to sort the ordered dictionary for the output, increasing the time complexity.

A history hashmap allows to quickly identify previous transactions, but only the latest ones are stored in order to save space.

"""

from collections import OrderedDict

def parse_raw_transaction(transaction):
    name, amount, location, time = transaction.split('|')
    time = int(time)
    amount = int(amount)
    return (name, amount, location, time)

def getSuspiciousList(transactions):
    if not transactions: return []
    fraudulent_amount = 3000
    
    # detected frauds
    fraudulent = OrderedDict()   
    
    # latest transaction history
    history = {}
    
    for transaction in transactions:
        # parses raw transaction
        name, amount, location, time = parse_raw_transaction(transaction)
        
        # a transaction spending more than $3000, fraud detected
        if amount > fraudulent_amount:
            if name not in fraudulent: 
                fraudulent[name] = time
            
            if name in history:
                h_time, h_location = history[name]
                if abs(time - h_time) < 60:
                    fraudulent[name] = h_time
                    
        # potential regular transaction
        else:
            # stores history
            if name not in history:
                history[name] = (time, location)
                
            # checks previous transactions to detect fraud
            else:
                h_time, h_location = history[name]
                
                # fraud detected,  previous transaction happened less than an hour in different place
                if h_location != location and abs(time - h_time) < 60:
                    if name not in fraudulent: fraudulent[name] = h_time
                else:
                    history[name] = (time, location)
    
    # outputs sorted by time
    return sorted(fraudulent, key = fraudulent.get)
        

























"""
Time O( n lg n)
Space O(2n) -> O(n)

The algorithm converts each entry into minutes from time 0:00 and after 24:00 (mirrored time, to fulfill cycles)
Sorts these entries and returns the least difference
"""

def parse_time_to_minutes(raw_time):
    """ Parses time in format HH:MM and converts this into minutes """
    hour, minute = list(map(int, raw_time.split(':')))
    return to_minutes(hour, minute)

def to_minutes(hour, minute):
    """ Converts hour, minute into minutes """
    return hour * 60 + minute
    
def getMinTimeDifference(times):
    if not times: return 0
    over_24h = to_minutes(24, 0)
    
    size = len(times)
    sorted_times = []
    least_diff = float("inf")    
    
    for raw_time in times:
        # parses time and converts to minutes
        minutes = parse_time_to_minutes(raw_time)
        
        # insert times into a list, regular time and after 24h
        sorted_times.append(minutes)
        sorted_times.append(minutes + over_24h)
    sorted_times.sort()
    
    # Finds least difference
    for i in range((size * 2) - 1):
        diff = abs(sorted_times[i] - sorted_times[i + 1])
        least_diff = min(least_diff, diff)
        
    return least_diff
    
    