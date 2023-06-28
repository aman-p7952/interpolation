    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:41:56 2022

@author: aman
"""

#!/usr/bin/python
import psycopg2
from .config import config

def connect(command):
    """ Connect to the PostgreSQL database server """
    conn = None
    data = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        cur.execute(command)

        # display the PostgreSQL database server version
        data = cur.fetchone()
    
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')
    return data

if __name__ == '__main__':                                                                                          
    connect()
