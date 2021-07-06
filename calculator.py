### make simpole calculator with python
def Calculator(value1,value2,op):
    if op =="*":
        result = value1 * value2
        return result
    elif op =="/":
        result = value1/value2
        return result   
    elif op =="-":
        result = value1 - value2
        return result
    elif op == "+":
        result = value1 + value2
        return result
    elif op =="%":
        result = value1 % value2
        return result
    else:
        return "This founction don't work."   
    
Inp =input("Enter the value:")
inp = list(Inp)        
val1 = []
op =""
val2 = []

for i in inp:
    if i not in ["*","-","+","/","%"]:
        val1.append(i)
    else:    
        op = i
        break
for i in range(len(inp)-1,0,-1):
    if inp[i] not in ["*","-","+","/","%"]:
        val2.append(inp[i])
    else:
        break
extra_arr =[]    
for i in range(len(val2)-1,-1,-1): ## i don't know why list reverse function don't work. 
    extra_arr.append(val2[i])
   
value1 = int("".join(val1))
value2 = int("".join(extra_arr))  

print("Result = ",Calculator(value1,value2,op)) 
 
