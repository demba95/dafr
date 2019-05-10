#!/usr/bin/python
"""Python module that receives TCP requests."""

import socket
import MySQLdb

#Instance t2.large proxy
host = '172.31.32.190'
port = 5001


def main():
    """Main."""
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)  # Listen to one connection
    c, addr = s.accept()
    print 'connection from: ' + str(addr)

    while True:
        data = c.recv(2048)  # Max bytes
        if not data:
            break
        print 'from connected user: ' + str(data)
        data = str(data)

        # TO DO ...

        # Implement a function that parses received data

        type, command = parse_data(data)

        if type == 'insert':
            hit_master(data)
        else:
            my_pattern(command)
        

    c.close()


def hit_master(data):
    # Connect to MySQL Cluster
    database = MySQLdb.connect(host="172.31.17.24",port=3306,user="clusteruser",passwd="Aminata99",db="clusterdb")
    # Hit the database based on the algorithm
    # TO DO ...
    cHandler = database.cursor()
    values =str(data.split(","))
    cHandler.execute("INSERT INTO DATADUMP VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",values)



def parse_data(data):
    """Function that takes the data and parses it."""
    type,command = map(str.strip, data.split(',', 1))
    # TO DO ...
    # Implement a function that parses the data and detects type of command
    return type, command


#Poxy pattern
def my_pattern():
    """Implement algorithm of the pattern here."""
    # Connect to MySQL Cluster
    database = MySQLdb.connect(host="172.31.17.24",port=3306,user="clusteruser",passwd="Aminata99",db="clusterdb")
    # Hit the database based on the algorithm
    # TO DO ...
    cHandler = database.cursor()
    values =str(data.split(","))

    cHandler.execute("SELECT * FROM DATADUMP")
    results = cHandler.fetchall()
    print items[0]


if __name__ == '__main__':
    main()
