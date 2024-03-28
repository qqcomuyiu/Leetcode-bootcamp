from collections import defaultdict, deque
import pdb
class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        # 构建站点到公交路线的映射
        stops_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stops_to_routes[stop].add(i)
        print(stops_to_routes)
        # 已访问路线集合
        visited_routes = set()
        # 待搜索队列，包含（当前站点，乘坐的公交车数量）
        queue = deque([(source, 0)])
        pdb.set_trace()
        while queue:
            current_stop, buses_taken = queue.popleft()
            if current_stop == target:
                return buses_taken
            # 遍历当前站点的所有公交路线
            for route_index in stops_to_routes[current_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    # 将该路线的所有站点加入待搜索队列
                    for next_stop in routes[route_index]:
                        queue.append((next_stop, buses_taken + 1))
        
        # 如果无法到达目的地
        return -1


s=Solution()
print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))







class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out=""
        snum,schr,sp=[],[],[]
        tempn=""
        tempc=""
        for i in s:
            if i.isnumeric():
                tempn+=i
              
            elif i.isalpha():
                tempc+=i
            else:
                if i=="[":
                    snum.append(tempn)
                    tempn=""
                    schr.append(tempc)
                    tempc=""
                else:
                    tempc = schr.pop() + int(snum.pop()) * tempc
        print(schr)
        return tempc 



            

class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: ints
        :rtype: int
        """
        q=[]
        i=0
        person=[i,delay+1,forget+1]
        q.append(person)
        for k in range(n):
            for node in q:
                if node[1]!=0: node[1]-=1
                node[2]-=1
            t=0
            temp=[]
            while t<len(q):
                if q[t][2]==0:
                    del q[t]
                    continue
                if q[t][1]==0:
                    i+=1
                    temp.append([i,delay,forget])
                t+=1
            for e in temp:
                q.append(e)
            
    
        return len(q)

