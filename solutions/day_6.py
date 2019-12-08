from dijkstar import Graph, find_path

def read_orbits(data_str):
    orbits = data_str.split('\n')
    orbit_tree = {}
    for orbit in orbits:
        parent, child = orbit.split(')')
        if child in orbit_tree:
            raise Exception('Cannot orbit more than one planet')
        else:
            orbit_tree[child] = parent
    return orbit_tree


def _count_helper(orbit_tree, planet):
    if planet not in orbit_tree:
        return 0
    else:
        return 1 + _count_helper(orbit_tree, orbit_tree[planet])


def count_orbits(orbit_tree):
    return sum([_count_helper(orbit_tree, c) for c in orbit_tree.keys()])


def sol_6(data_str):
    orbit_tree = read_orbits(data_str)
    return count_orbits(orbit_tree)


def _thing(orbit_tree, planet):
    if planet not in orbit_tree:
        return []
    else:
        return [planet] + _thing(orbit_tree, orbit_tree[planet])


def sol_6_b(data_str):
    orbit_tree = read_orbits(data_str)
    g = Graph()
    for planet in orbit_tree:
        g.add_edge(orbit_tree[planet], planet, 1)
        g.add_edge(planet, orbit_tree[planet], 1)
    path = find_path(g, 'YOU', orbit_tree['SAN'])
    return path.total_cost - 1