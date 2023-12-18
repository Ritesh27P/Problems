class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict1 = {k:v for (k, v) in paths}
        curr = paths[0][0]
        while True:
            if dict1.get(curr):
                curr = dict1[curr]
            else:
                return curr

        