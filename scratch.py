str="hello (this only please)..(not this)."

print(str,str[6])
print(str[6+1:][:str[6+1:].index(")")])
print(str[6+1:].index(")"))
print(str[6+2+str[6+1:].index(")")])