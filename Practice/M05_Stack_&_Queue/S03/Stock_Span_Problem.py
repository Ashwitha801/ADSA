class StockSpanner:

    def __init__(self):
        self.stack = []

        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        
        return 
#Input
in1 = ["StockSpanner","next","next","next","next","next","next"]
in2 = [[],[100],[80],[60],[70],[60],[75],[85]]
res = []
obj = None
for x,y in zip(in1,in2):
    if x == "StockSpanner":
        obj = StockSpanner()
        res.append(None)
    else:
        res.append(obj.next(y[0]))

print(res)


        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)