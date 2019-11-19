import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) == 5:
        user_ptr_id, reputation, gold, silver, bronze = line

        writer.writerow([user_ptr_id, "A", reputation, gold, silver, bronze])

    elif len(line) == 19:
        post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, \
        added_at, score, state_string, last_edited_id, last_activity_by_id, \
        last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line

        writer.writerow([author_id, "B", post_id, title, tagnames, added_at, score])
