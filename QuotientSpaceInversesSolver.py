from math import gcd
import re

def parse(problem_statement):
    modulus_str = re.search(r'Z/(\d+)Z', problem_statement)
    # modulus_str cannot be empty 
    # If empty, if not None because modulus_str == None when nothing is found
    if not modulus_str:
    	raise ValueError("Invalid format. Expected 'Z/mZ'")
    # modulus is a map (generator) that returns one elem at a time, turning each from str to int type. 
    # Ex. modulus_str.groups() == ('16',) and modulus == <map object at memory location>
    modulus = map(int, modulus_str.groups())
    # Return the first element (only one expected)
    # Ex. return 16, type is int
    return next(modulus)
    

def find_unit_group(modulus):
    unit_group = set()
    # for num in range(1, 16) which is [1, 2, 3, ..., 15]
    for num in range(1, modulus):
        # gcd == 1 means num and modulus coprime, num has an invertible element.
        # Ex. gcd(3, 16) == 1
        if gcd(num, modulus) == 1:
            # Ex. unit_group.append(3)
            # unit_group == [1, 3]
            unit_group.add(num)
    return unit_group
    
def find_orders_and_inverses_for_units(unit_group, modulus):
    orders = dict()
    inverses = dict()
    # Ex. num == 5 in {1, 3, 5, 7, 9, 11, 13, 15}
    for num in unit_group:
        order = 1
        
        # powered == 5 
        # for getting order
        powered = num
        
        # powered_one_less == 1
        # for getting inverse because inverse of a times a == 1.
        # Take inverse of unit to be unit ** (orders[unit] - 1).
        powered_one_less = 1
        
        # while 5 != 1
        while powered != 1:
            # powered = (5 * 5) % 16 == 9
            powered = (powered * num) % modulus
            # powered_one_less = (1 * 5) % 16 == 5
            powered_one_less = (powered_one_less * num) % modulus
            # order += 1 == 2
            order += 1
        # while 9 != 1
            # powered = (9 * 5) % 16 == 13
            # powered_one_less = (5 * 5) % 16 == 9
            # order += 1 == 3
        # while 13 != 1
            # powered = (13 * 5) % 16 == 1
            # powered_one_less = (9 * 5) % 16 == 13
            # order += 1 == 4
        # while 1 != 1
            # break
    
        # orders[5] = 4
        orders[num] = order
        # inverses[5] = 13
        inverses[num] = powered_one_less

    # orders == {1:1, 3:4, 5:4, 7:2, 9:2, 11:4, 13:4, 15:2}
    # inverses == {1:1, 3:11, 5:13, 7:7, 9:9, 11:3, 13:5, 15:15}
    return orders, inverses
    

def main():
    # problem_statement = Z/16Z
    problem_statement = input('What is your quotient space? Type in the format of Z/16Z exactly. Regular expression does the parsing.\n')
    # modulus = 16, type is int
    modulus = parse(problem_statement)
    
    # UNIT GROUP 
    # (group of all invertible elements in this quotient space)
    # unit_group is a set, but sets preserve the appended element order in newer Pythons, so we can use it reproducibly. 
    unit_group = find_unit_group(modulus)
    # Unit group: {1, 3, 5, 7, 9, 11, 13, 15}
    print(f'Unit group: {unit_group}')
    
    # ORDERS AND INVERSES
    # order of a is the power to which a is raised that results in 1. 
    orders, inverses = find_orders_and_inverses_for_units(unit_group, modulus)
    print(f'Orders of units: {orders}')
    print(f'Inverses of units: {inverses}') 
    
if __name__ == "__main__":
    main()