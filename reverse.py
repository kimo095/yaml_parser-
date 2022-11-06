import yaml

with open('string.yaml','r') as read_file:
    contents = yaml.safe_load(read_file)

  
inputStr = contents
result = ''

for i in range(len(inputStr)-1,-1,-1):
    result = result + inputStr[i]

with open('output.yaml','w') as dump_file:
    yaml.dump(result, dump_file)
print(result)