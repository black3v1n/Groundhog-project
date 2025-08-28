import math

# global variable
temperature_values = [];temperature_copy = [];temperature_copy_two = []
list_g = []; aberration_values = []
my_tuple_list = []

def calcul_aberration_value():
    c = 0; a = 0
    result = []
    #loop to calcul aberration
    while a < len(temperature_values)-2:
        a+=1
        one = (temperature_values[(a-1)] + temperature_values[(a+1)])/2
        two = temperature_values[a]
        final_value = abs(one-two)
        my_tuple_list.append((final_value, two)) #add a tuple in the list where the first element is the final_value
    my_tuple_list_sorted = sorted(my_tuple_list, key=lambda x: x[0], reverse= True) #sorted the tuple list with the first element of tuple
    for _ in range(5):
        result.append(my_tuple_list_sorted[_][1])
    return result
    
def calcul_g(t):
    res = 0
    for _ in list_g:
        res += _
    list_g.remove(list_g[0])
    return res/t

def calcul_r(t):
    res = 0
    if (len(temperature_values) >= t):
        res = temperature_values[len(temperature_values)-1] - temperature_values[len(temperature_values)-(t+1)]
        if temperature_values[len(temperature_values)-(t+1)] == 0:
            return 1000
        else:
            res = res / abs(temperature_values[len(temperature_values)-(t+1)])
            return res*100

def calcul_s():
    sum_t_pow = 0; sum_t = 0
    for _ in temperature_copy_two:
        sum_t_pow += math.pow(_, 2)
        sum_t += _
    len_t = len(temperature_copy_two)
    cal_one = sum_t_pow/len_t
    cal_two = math.pow((sum_t/len_t),2)
    temperature_copy_two.remove(temperature_copy_two[0])
    return math.sqrt(cal_one-cal_two)
            
def main_control(count, day):
    if (len(temperature_copy) == 2):
        total = (temperature_copy[1]-temperature_copy[0])
        list_g.append(total if total > 0 else 0)
        temperature_copy.remove(temperature_copy[0])
