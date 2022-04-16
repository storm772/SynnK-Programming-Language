# Change to where script.sk is
location = "C:/Users/SynnK/Desktop/Programming language/"

file = open(f'{location}script.sk', 'r')

count = 0
debugMode = False 
envTypes = ('DEBUG')

# Delete a index from a list (string)
def extract(l = list, n = int):
    del l[n]
    return " ".join(l)

# Return all the values after a index (string)
def valuefrom(l = list, n = int):
    return " ".join(l[n:])

# Command Retriever (boolean)
def command(l, name = str):
    return bool(l != '' and l.split()[0] == name)

def read():
    global count
    global debugMode 
    global envTypes

    for cline in file.readlines():
        count += 1

        line = cline.strip()

        if line != '' and line.startswith(';'):
            isENV = bool(line.split()[0][1:] == 'ENV')
            if isENV:
                if len(line.split()) == 2 and line.split()[1] == 'DEBUG':
                    debugMode = True
                if len(line.split()) == 1:
                    print('no environment mode specified')
                elif line.split()[1].endswith(envTypes) == False:
                    print(f'LINE {count} | AssertError: Environment "{line.split()[1]}" is not a valid env mode.\n      -> Line: "{line.strip()}"   <- Valid Env Modes: {envTypes}')
                
                if debugMode:
                    print(f'/!\   Using {line.split()[1]} mode')

        if debugMode:
            print(f'{count:>2} | {line.strip():>3}')

        if command(line, '//'):
            if debugMode:
                print(f'    Found a note: {line.split("//")[1].strip()}')
        
        if command(line, 'SET'):
            s = line.removeprefix('SET').strip().split()
            if s[0].isdigit() == True:
                print(f'LINE {count} | AssertError: {s[0]} is a INTEGER, expected STRING.\n     -> Line: "{line.strip()}"')
            if len(line.split()) == 2:
                print(f'LINE {count} | AssertError: {s} does not have any value.\n      -> Line: "{line.strip()}"')
            else:
                if valuefrom(s, 1).isdigit() == False and '"' not in valuefrom(s, 1):
                    print(f'LINE {count} | TypeError: "{valuefrom(s,1)}" is not a known type.\n      -> Line: "{line.strip()}"')
            
            exec(f"{s[0]} = {valuefrom(s, 1)}")

            if debugMode:
                print(f'    Variable name: {s[0]}\n    Value Stored: {valuefrom(s,1)}')

        if command(line, 'LOG'):
            if '"' in line:
                print(f'>>> {line.split("LOG")[1].strip()}')
            else:
                try:
                    exec(f"print({line.split('LOG')[1].strip()})")
                except TypeError as e:
                    print(e)
read()
