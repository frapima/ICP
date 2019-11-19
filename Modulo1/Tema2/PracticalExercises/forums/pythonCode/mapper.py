import sys
import csv
import re


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19:
        continue

    post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, \
    added_at, score, state_string, last_edited_id, last_activity_by_id, \
    last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line

    counter = body.count('.') + body.count('?') + body.count('!')
    if counter > 1 or not body.endswith(('.', '?', '!')):
        continue

    print(post_id + '\t' + title + '\t' + tagnames + '\t' + author_id + '\t' + body + '\t' + \
          node_type + '\t' + parent_id + '\t' + abs_parent_id + '\t' + added_at + '\t' + \
          score + '\t' + state_string + '\t' + last_edited_id + '\t' + last_activity_by_id + '\t' + \
          last_activity_at + '\t' + active_revision_id + '\t' + extra + '\t' + extra_ref_id + '\t' + \
          extra_count + '\t' + marked)
