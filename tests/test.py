web = open("web.txt","r")
nonWeb = open("nonWeb.txt","r")

print web.read().split("\n")
print nonWeb.read().split("\n")