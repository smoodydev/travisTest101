import os

# ive installed a library : pip install dj-database-url psycopg2. It allows us to do is to connect to a database using a URL, rather than the standard database driver that Django uses.

#  we're not going to upload this file to GitHub. This is just for local testing. 
os.environ.setdefault('SECRET_KEY', 'wjzy^vfn00@xk-+nk2a5-!8eqgxd*vlu*b$ux&$^cu)pe_2zd#')

# Purely for local testing
os.environ.setdefault('DATABASE_URL', 'postgres://yspbpjzapuodbx:d9ff13a8fdf84aefcea2b45317811072aaf0fca9c34a4904e2b484271a741887@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/d7f1g8kdl1dsrn')




