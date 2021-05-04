import re
print("""Hello! welcome to madlib game
you will be asked to add a name, verb, or Adjective and a funny sentences """)

def read_template(path):
    with open(path, 'r') as game:
        return game.read()

def parse_template(str):
    tuple1 = ()
    keyList = list(tuple1)
    end = 0
    repetitions = str.count('{')
    for i in range(repetitions):
        start = str.find('{', end) + 1
        end = str.find('}', start)
        key = str[start : end]
        keyList.append(key)
    pattern = r"\{(.*?)\}"
    new = re.sub(pattern, "{}", str)
    t1 = tuple(keyList)
    return new, t1

tuple2 = ()
responseList = list(tuple2)
actual_stripped, actual_parts = parse_template(read_template("assets/make_me_a_video_game_template.txt"))

for i in range(len(actual_parts)):
    response = input(actual_parts[i])
    responseList.append(response)

t2 = tuple(responseList)

def merge(str, tup):
    return str.format(tup)

print(merge(actual_stripped, t2))
    
