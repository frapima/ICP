import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

mykey = None # inventado

topN = 2

#Una lista que incluye cada linea y su longitud en forma de sublista
lineWithLength=[]

def getLength(line):
    return line[1]

# PON TU CODIGO AQUÍ
for line in reader:
    if len(line) != 19:
        continue

    post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, \
    added_at, score, state_string, last_edited_id, last_activity_by_id, \
    last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line

    length = len(body)

    lineWithLength.append([line, length])

lineWithLength.sort(key=getLength, reverse=True)
lineWithLength = lineWithLength[:topN]

for data in lineWithLength:
    line, length = data

    print(str(line) + '\t' + str(length))
