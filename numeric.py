import re, random

def arith_operation(arith_str: str):
    arith_str = arith_str.replace('module', '%')
    arith_str = arith_str.replace('integer division', '//')
    arith_str = arith_str.replace('exponent', '**')
    arith_str = arith_str.replace('bit shift left', '<<')
    arith_str = arith_str.replace('bit shift right', '>>')
    arith_str = arith_str.replace('exclusive or', '^')
    try:
        return str(eval(arith_str))
    except:
        return "Say Again"

def logical_operation(logical_str: str):
    logical_str = logical_str.replace('true', 'True')
    logical_str = logical_str.replace('false', 'False')
    try:
        return eval(logical_str)
    except:
        return "Say Again"
    
def random_pick(query: str):
    query = "".join(query.split())
    query = re.split(r'or', query)
    return random.choice(query)

def roll_dice(query: str, resp='Sure, here are the dices:'):
    
    query = [num for num in re.findall(r'[0-9]*', query) if num]
    if len(query) > 1:
        num_dice = int(query[0])
        type_dice = int(query[1])
    elif len(query) == 1:
        num_dice = random.randint(1, 10)
        type_dice = int(query[0])
    else:
        num_dice = random.randint(1, 10)
        type_dice = random.choice([6, 12])
        
    for _ in range(num_dice):
        resp = resp + ' ' + str(random.randint(1, type_dice))
    return resp

def main(text: str):
    if 'dice' in text:
        return roll_dice(text)
    elif re.search(r'[+|\-|/|*|//]|module|integer division|exponent|bit shift|exclusive or', text):
        return arith_operation(text)
    elif re.search(r'true|false', text.lower()):
        return logical_operation(text)
    elif 'or' in text:
        return random_pick(text)