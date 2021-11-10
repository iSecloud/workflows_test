import json
import os
import random
from typing import Dict

def generate_random_value(len: int) -> str:
    return "".join([chr(random.randint(96, 26 + 96)) for i in range(len)])

def generate_random_dict(dep: int, dict: Dict) -> Dict:
    if dep <= 0:
        return dict

    rd_iter = random.random()
    
    while rd_iter < 0.5 and dep >= 0:
        key = generate_random_value(random.randint(0, 20))
        value = generate_random_value(random.randint(0, 20))
        dict[key] = value
        rd_iter = random.random()
        dep -= 1
    
    dep -= 1
    key = generate_random_value(random.randint(0, 20))
    value = generate_random_dict(dep, {})
    dict[key] = value

    return dict


dict = json.dumps(generate_random_dict(1000, {}))

with open("dict_info.txt", "w") as f:
    f.write(dict)