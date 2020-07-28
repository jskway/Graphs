class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        self.vertices[v] = []

    # Edges will store a 'child' or 'parent' relation along with the ID
    def add_edge(self, v1, v2, relation):
        self.vertices[v1].append((v2, relation))

    def get_neighbors(self, v):
        return self.vertices[v]

    def is_parent(self, edge):
        if edge[1] == 'parent':
            return True
        else:
            return False

    def dft_ancestors(self, vertex, paths, longest, path=None):
        # If no path was passed in, initialize an array
        if path is None:
            path = []

        # Create a new path list with the current vertex added to the end
        path = path + [vertex]

        # Get the neighbors of the current vertex
        neighbors = self.get_neighbors(vertex)

        # Filter out the children, since we're only looking for ancestors
        # Convert the result to a list since filter returns an iterable without
        # a len property
        parents = list(filter(self.is_parent, neighbors))

        # If we're at the earliest ancestor
        if len(parents) == 0:
            # If this path is the longest
            if len(paths) > longest:
                # Update the longest value
                longest = len(paths)
                # Replace whatever is in the paths list with our longest path
                paths = [path]
            else:
                # Otherwise just append the path to our list of paths
                paths.append(path)

            # Return because there are no parents left to recurse through
            return

        # Recurse through the parents until we reach the earliest ancestor
        for parent in parents:
            self.dft_ancestors(parent[0], paths, longest, path)

def earliest_ancestor(ancestors, starting_node):
    # Create a graph
    g = Graph()

    # Iterate over ancestors
    for ancestor in ancestors:
        parent, child = ancestor;

        if parent not in g.vertices:
            g.add_vertex(parent)

        g.add_edge(parent, child, 'child')

        if child not in g.vertices:
            g.add_vertex(child)

        g.add_edge(child, parent, 'parent')

    # Set up a list to store paths
    paths = []

    # Variable to store length of longest path
    longest = 0

    # Perform a DFT over the starting_node's ancestors
    g.dft_ancestors(starting_node, paths, longest)

    # If there are multiple 'longest' paths
    if len(paths) > 1:
        # Set a list to store the oldest ancestors
        ancestors = []

        # Iterate through the paths
        for path in paths:
            # Append the ancestor to the list
            ancestors.append(path[-1])

        # Return the ancestor with the lowest ID
        return min(ancestors)

    # If there is only one item in path, there was no ancestor
    if len(paths[0]) == 1:
        # So we return -1
        return -1
    else:
        # Otherwise, return the last ancestor in the path
        return paths[0][-1]

#test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

#print(earliest_ancestor(test_ancestors, 3)) # should print 10
