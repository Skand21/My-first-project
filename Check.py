def start_end(x):
    if x == 1:
        return one()
    if x != 1:
        return _not_one_()

def one():
    return print(1)
def _not_one_():
    return print(-879465132)

x = 12
start_end(x)
