"""
This file is for parsing function names and types into a list to be exported to the main parser
This is considered a separate script to the main project and is purely to assist with development
It reads function names and types (nular, unary & binary) from this file:
https://github.com/intercept/intercept/blob/1.92/src/client/headers/client/sqf_assignments.hpp
I do not own the rights to the above file.
"""

import urllib3

functions = {
    'unary': list(),
    'binary': list(),
    'nular': list(),
}
url = 'https://raw.githubusercontent.com/intercept/intercept/1.92/src/client/headers/client/sqf_assignments.hpp'
req = urllib3.PoolManager().request('GET', url)

if req.data:
    for line in req.data.split(b'\n'):
        if line.startswith(b'__'):
            func_type, func_name, *_ = line[7:].decode('utf-8').split('__')
            functions[func_type].append(func_name)

print(f'Unary functions:\n{functions.get("unary")}')
print(f'Binary functions:\n{functions.get("binary")}')
print(f'Nular functions:\n{functions.get("nular")}')
