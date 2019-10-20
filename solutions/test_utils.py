import os 
import re
import sys
from timeit import timeit

project_root = os.path.abspath(os.path.join(__file__, '../..'))
sys.path.append(project_root)

from structures.graph import numeric_graph
def test(data=None, loader=None, times=10):
    data = data if os.path.exists(data) else os.path.join(project_root, data)
    if os.path.isfile(data):
        files = [data]
        pairs = [(os.path.basename(data), data, 0)]
    else:
        files = os.listdir(data) 
        pairs = ((file, f"{data}/{file}", os.path.getsize(f"{data}/{file}")) for file in files)
    padd = max(map(len, files))

    def wrap(function):
        result = dict()
        for file_name, file, _ in sorted(pairs, key=lambda x: x[2]):
            solution, args = loader(file)
            res = []
            def run():
                res.append(function(*args))
            sys.stdout.write(file_name.rjust(padd))
            time = timeit(run, number=times)
            result[file] = { "time": time, "passed": res[0] == solution }
            passed = '✔' if res[0] == solution else '❌'
            time = str(round(time / times, 5)).rjust(10)
            print(f" {passed} ⌚ {time}")
            if res[0] != solution:
                print('solution:', solution, 'result:', res[0])
        return result
    return wrap


def load_graph(file, directed=False):
    V, L = 0, []
    solution = None
    with open(file, 'r') as f:
        for l in f.readlines():
            s = l.split()
            if len(s) < 1:
                continue
            if s[0] == 'c':
                solution = int(re.match(r"c.*solution.*?(\d+)", l).group(1))
            elif s[0] == 'p':
                V = int(s[2]) + 1
            elif s[0] == 'e':
                (x, y, c) = (int(s[1]), int(s[2]), int(s[3]))
                # (x, y) = (min(a, b), max(a, b))
                L.append((x, y, c))
    return solution, [numeric_graph(V, L, directed=directed)]

def load_directed_graph(file):
    return load_graph(file, directed=True)
