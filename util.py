
f = open("/Users/admin/Desktop/app_id.txt")
line = f.readline()
l = []
while line:
    l.append(int(line.strip()))
    line = f.readline()
f.close()
print(l)