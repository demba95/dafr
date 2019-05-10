#A executer 5 fois


#Standalone
sudo sysbench --test=oltp_read_write --table-size=10000 --mysql-db=sakila --mysql-user=root --mysql-password=Aminata99 --max-time=60 --max-requests=0 --num-threads=8 --db-driver=mysql run

#Cluster
sudo sysbench --test=oltp_read_write --table-size=10000 --mysql-db=sakila --mysql-user=clusteruser --mysql-password=Aminata99 --max-time=60 --max-requests=0 --num-threads=8 --db-driver=mysql --mysql-storage-engine=ndbcluster run
