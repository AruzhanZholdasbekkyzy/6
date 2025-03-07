def all_true(tup):
    return all(tup)  

t = (True, True, 1, "Hello")  
print(f"Are all elements in the tuple true? {all_true(t)}")

mytup = (True, True, False)
mytup2 = (True, True, True)
print(all(mytup))
print(all(mytup2))