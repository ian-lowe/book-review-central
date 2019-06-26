import psycopg2
conn = psycopg2.connect("host= dbname= password=")
cur = conn.cursor()

with open('books.txt', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'books', sep='\t')
    conn.commit()