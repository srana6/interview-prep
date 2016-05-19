import math

x = 0
y = 1

def eucledian_distance(departure, destination):
    return math.sqrt( pow(destination[x] - departure[x], 2) + pow(destination[y] - departure[y], 2))



def round_coord(point1, point2, path):
    if not float(point1[x]).is_integer():


    elif float(point1[y]).is_integer():


    if not float(point1[x]).is_integer():
        point1_x_down = [math.floor(point1[x]), point1[y]]
        point1_x_up = [math.ceil(point1[x]), point1[y]]
        
        if eucledian_distance(point1_x_down, point2) < eucledian_distance(point1_x_up, point2):
            path += abs(point1[x] - point1_x_down[x])
            point1 = point1_x_down
        elif eucledian_distance(point1_x_down, point2) > eucledian_distance(point1_x_up, point2):
            path += abs(point1[x] - point1_x_up[x])
            point1 = point1_x_up
        else:
            if abs(point1[x] - point1_x_down[x]) < abs(point1[x] - point1_x_up[x]):
                path += abs(point1[x] - point1_x_down[x])
                point1 = point1_x_down
            else:
                path += abs(point1[x] - point1_x_up[x])
                point1 = point1_x_up
    
    elif not float(point1[y]).is_integer():
        point1_y_down = [point1[x], math.floor(point1[y])]
        point1_y_up = [point1[x], math.ceil(point1[y])]    
        
        
        if eucledian_distance(point1_y_down, point2) < eucledian_distance(point1_y_up, point2):
            path += abs(point1[y] - point1_y_down[y])
            point1 = point1_y_down
        elif eucledian_distance(point1_y_down, point2) > eucledian_distance(point1_y_up, point2):
            path += abs(point1[y] - point1_y_up[y])
            point1 = point1_y_up
        else:
            if abs(point1[y] - point1_y_down[y]) < abs(point1[y] - point1_y_up[y]):
                path += abs(point1[y] - point1_y_down[y])
                point1 = point1_y_down
            else:
                path += abs(point1[y] - point1_y_up[y])
                point1 = point1_y_up
                
    return (point1, point2, path)
        

    

def perfectCity(departure, destination):
    path = 0        
    departure, destination, path = round_coord(departure, destination, path)
    destination, departure, path = round_coord(destination, departure, path)
        
    path += abs(departure[x] - destination[x])
    path += abs(departure[y] - destination[y])
    
    return float(("%.2f" % path))
        
        
    
    
    


    
    
    


        
    
    
    


    
    
    

departure =   [0.0, 0.0]
destination = [3, 3]

print (perfectCity(departure, destination))