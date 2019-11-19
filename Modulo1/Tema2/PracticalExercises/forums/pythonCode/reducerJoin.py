import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

currentUser = None

id = title = tagnames = author_id = parent_id = abs_parent_id = added_at = score = reputation = gold = silver = bronze = ""
source = None
user_ptr_id = ""

for line in reader:
    if len(line) == 6 and line[1] == "A":
        user_ptr_id, source, reputation, gold, silver, bronze = line

    elif len(line) == 7 and line[1] == "B":
        author_id, source, id, title, tagnames, added_at, score = line
        if user_ptr_id == author_id:
            writer.writerow([id, title, tagnames, author_id, added_at, score, reputation, gold, silver, bronze])
