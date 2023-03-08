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
    num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
    num_dice = re.search(r'one|two|three|four|five|six|seven|eight|nine|ten', query)
    if num_dice:
        num_dice = num_dict[num_dice.group()]
        for _ in range(num_dice):
            resp = resp + ' ' + str(random.randint(1, 6))
    else:
        for _ in range(random.randint(1, 10)):
            resp = resp + ' ' + str(random.randint(1, 6))
    return resp

def main(text: str):
    if re.search(r'[+|\-|/|*|//]|module|integer division|exponent|bit shift|exclusive or', text):
        return arith_operation(text)
    elif re.search(r'true|false', text.lower()):
        return logical_operation(text)
    elif 'dice' in text:
        return roll_dice(text)
    elif 'or' in text:
        return random_pick(text)