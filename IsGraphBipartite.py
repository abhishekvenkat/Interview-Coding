class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        one_half, second_half = [0],[]
        stack = [] + graph[0]
        
        def recurse(graph, one_half, second_half, stack):
            while stack:
                
                stack = list(set(stack))
                merged_list = one_half + second_half
                elem = stack.pop(0)
                if elem in merged_list: continue
                    
                # print one_half, type(one_half)
                # print second_half, type(second_half)
                # print stack
                # print elem
                
                if not set(graph[elem]).isdisjoint(one_half):
                    if not set(graph[elem]).isdisjoint(second_half):
                        return False
                    else:
                        second_half.append(elem)
                        stack = stack + graph[elem]
                        
                elif not set(graph[elem]).isdisjoint(second_half):
                    one_half.append(elem)
                    stack = stack + graph[elem]
                    
                else:
                    return recurse(graph, one_half + [elem], second_half, stack + graph[elem]) or recurse(graph, one_half, second_half + [elem], stack + graph[elem])
            
            
            merged_list = one_half + second_half
            i = len(graph)
            for j in xrange(len(graph)): 
                if j not in merged_list:
                    i = j
            # print i
            if i == len(graph): return True
            else: return recurse(graph, one_half + [i], second_half, stack + graph[i]) or recurse(graph, one_half, second_half + [i], stack +graph[i])

                    
            
        return recurse(graph, one_half, second_half, stack)
        
