"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Make a set to track visited vertices
        visited = set()

        # Set up our queue
        q = Queue()

        # Enqueue the starting vertex
        q.enqueue(starting_vertex)

        # While the queue is not empty
        while q.size() > 0:

            # dequeue the first vertex
            current_vertex = q.dequeue()

            # Check if the current vertex was visited
            if current_vertex not in visited:
                # Add it to visited and print it
                visited.add(current_vertex)
                print(current_vertex)

                # Iterate over current_vertex's neighbors and
                # enqueue them
                for neighbor in self.get_neighbors(current_vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Make a set to track visited vertices
        visited = set()

        # Set up a stack
        s = Stack()

        # Push the starting vertex onto the stack
        s.push(starting_vertex)

        # While the stack is not empty
        while s.size() > 0:

            # Pop off the top vertex
            current_vertex = s.pop()

            # Check if the current vertex was visited
            if current_vertex not in visited:
                # Add it to visited and print it
                visited.add(current_vertex)
                print(current_vertex)

                # Iterate over current vertex's neighbors and
                # push them onto the stack
                for neighbor in self.get_neighbors(current_vertex):
                    s.push(neighbor)

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from vertex.

        This should be done using recursion.
        """
        # If visited is None, initialize it with a set
        if visited == None:
            visited = set()

        # If the vertex has not been visited
        if vertex not in visited:
            # Print it and add it to visited 
            print(vertex)
            visited.add(vertex)

            # Get the neighbors
            neighbors = self.get_neighbors(vertex)

            # Iterate through the neighbors
            for neighbor in neighbors:
                # And recurse for each neighbor
                self.dft_recursive(neighbor, visited)
        # Base Case: All vertexes have been visited
        else:
            return


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Initialize a set for keeping track of visited indices
        visited = set()

        # Initialize a path with the starting_vertex
        path = [starting_vertex]

        # Set up a queue  for enqueuing paths
        q = Queue()

        # Enqueue the path
        q.enqueue(path)

        # Iterate through the paths while the queue is not empty
        while q.size() > 0:
            # Dequeue the first path in the queue
            current_path = q.dequeue()

            # current_vertex is the last vertex in the current path
            current_vertex = current_path[-1]

            # If we're at the destination, return the current path
            if current_vertex == destination_vertex:
                return current_path

            # If we haven't visited the current vertex, add it to the visited set 
            if current_vertex not in visited:
                visited.add(current_vertex)

            # Iterate over the current vertex's neighbors  
            for neighbor in self.get_neighbors(current_vertex):
                # Make a copy of the current path
                neighbor_path = current_path.copy()
                # Add the neighbor to the current path
                neighbor_path.append(neighbor)

                # We're making a new path for each neighbor
                # so we can check which path is the shortest

                # enqueue the new path
                q.enqueue(neighbor_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize a set for keeping track of visited indices
        visited = set()

        # Initialize a path with the starting_vertex
        path = [starting_vertex]

        # Set up a stack for pushing paths
        s = Stack()

        # Push the path onto the stack
        s.push(path)

        # Pop off the latest path  while it's not empty
        while s.size() > 0:
            # Pop off the top path in the stack
            current_path = s.pop()

            # current_vertex is the last vertex in the current path
            current_vertex = current_path[-1]

            # If we're at the destination, return the current path
            if current_vertex == destination_vertex:
                return current_path

            # If we haven't visited the current vertex, add it to the visited set 
            if current_vertex not in visited:
                visited.add(current_vertex)

            # Iterate over the current vertex's neighbors  
            for neighbor in self.get_neighbors(current_vertex):
                # Make a copy of the current path
                neighbor_path = current_path.copy()
                # Add the neighbor to the current path
                neighbor_path.append(neighbor)

                # We're making a new path for each neighbor
                # so we can check which path is the shortest

                # push the new path onto the stack
                s.push(neighbor_path)


    def dfs_recursive(self, vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initialize a set to track visited vertices if None
        if visited == None:
            visited = set()

        visited.add(vertex)

        # Initialize a path list if None
        if path == None:
            path = []

        # Make a copy of the path
        # This prevents unwanted mutation when recursing through 
        # the current vertex's neighbors
        path = path.copy()

        # Append the vertex
        path.append(vertex)

        # If we're at the destination return the current path
        if vertex == destination_vertex:
            return path

        # Otherwise, iterate over the neighbors
        for neighbor in self.get_neighbors(vertex):
            # If the neighbor hasn't been visited
            if neighbor not in visited:
                # Get a new path by following the neighbor's edge
                new_path = self.dfs_recursive(neighbor, destination_vertex,
                                              visited, path)

                # new_path be not None only when the destination_vertex 
                # has been reached
                if new_path is not None:
                    return new_path

        # If  all neighbors have been visited for this vertex
        # and we're not at the destination_vertex
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
