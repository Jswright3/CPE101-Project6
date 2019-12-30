filepath = 'crimes.tsv'

line = open(filepath).readline()
cnt = 1
lines = []
while line:
   lines.append(line)
   line = open(filepath).readline()
   cnt += 1
return lines