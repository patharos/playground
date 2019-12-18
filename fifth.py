

def create_route():
    with open('routes') as r:
        return [crd.split(',') for crd in [line.rstrip('\n') for line in r]]


def adding_co(first, second):
    return [first[0]+second[0], first[1]+second[1]]


def check_direction_value(ind):
    if ind[0] == 'R':
        return [int(ind[1:]), 0]
    if ind[0] == 'L':
        return [(-1)*int(ind[1:]), 0]
    if ind[0] == 'U':
        return [0, int(ind[1:])]
    if ind[0] == 'D':
        return [0, (-1)*int(ind[1:])]


def create_vectors():
    routes = create_route()
    list_route = [[], []]
    for route, i in zip(routes, range(len(routes))):
        start_point = [0, 0]
        for move in route:
            start_point = adding_co(start_point, check_direction_value(move))
            list_route[i].append(start_point)
    return list_route


print('show me the first {} \n i drugie {}'.format(create_vectors()[0], create_vectors()[1]))