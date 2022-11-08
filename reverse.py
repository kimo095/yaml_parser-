import yaml

with open('string.yaml','r') as read_file:
    contents = yaml.safe_load(read_file)

  
inputStr = contents
result = ''

inputStr = contents.split()[::-1]
l = []
for i in inputStr:
    l.append(i)
result = (" ".join(l))
with open('output.yaml','w') as dump_file:
    yaml.dump(result, dump_file)
print(result)