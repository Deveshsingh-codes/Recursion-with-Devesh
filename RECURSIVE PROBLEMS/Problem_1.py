# Print 1 to n 
def print_number(n):
    if n ==1:
        print(1,end=" ")
        return
    print_number(n-1)
    print(n,end=" ")
    
print_number(10)