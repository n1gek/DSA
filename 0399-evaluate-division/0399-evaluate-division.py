from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # equations = [["a","b"],["b","c"]]
        # values = [2.0,3.0]
        # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

        graph = defaultdict(list)

        for i in range(len(values)):
            current_eqn = equations[i]
            first, second = current_eqn[0], current_eqn[1]
            # first/second = values[i]
            # a/b = 2
            graph[first].append((second, values[i]))
            graph[second].append((first, 1/values[i]))
            # {a: [(b:2), (c:3)]}
        
        res = []

        def hasPath(source, dest):
            if source not in graph:
                return -1
            if source == dest:
                return 1

            queue = deque([(source, 1.0)])  # ✅ queue stores tuple (node, accumulated_product)
            seen = set([source])

            while queue:
                curr, acc = queue.popleft()

                for neighbor in graph[curr]:  # neighbor is a tuple
                    key, val = neighbor

                    if key not in seen:
                        if key == dest:
                            return acc * val

                        queue.append((key, acc * val))  # ✅ use tuple
                        seen.add(key)

            return -1

                

        for q in queries:
            source, dest = q[0], q[1]

            res.append(hasPath(source, dest))
        
        return res



        