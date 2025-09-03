idx = 0

try:
    with open("infinite_nest.py", "w") as f:
        f.write("if True:")
    while True:
        with open("infinite_nest.py", "r") as f:
            data = f.read()
        data += "\n"
        for i in range(idx + 1):
            data += "   "
        data += "if True:"
        with open("infinite_nest.py", "w") as f:
            f.write(data)
        idx += 1
except:
    with open("infinite_nest.py", "r") as f:
        data = f.read()
    data += "\n"
    for i in range(idx + 1):
        data += "   "
    data += "print('poopie')"
    with open("infinite_nest.py", "w") as f:
        f.write(data)