f = open("./list_attr_cloth_trim.txt", 'r')

# 1: texture-related attributes
# 2: fabrci-related attributes
# 3: shape-related attributes
# 4: part-related attributes
# 5: style-related attributes
filtering = 1
number = 1
while True:
    line = f.readline().strip()
    if not line: break
    # print(str(count) + line)
    attr  = line[-1]
    attr_name = line[:-1]
    if(int(attr) == filtering):
        print(str(number)+" "+"name: "+attr_name.strip() + ", number: "+attr)
        print(attr_name.strip())
        number += 1

f.close()