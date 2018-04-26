import socket
import sys

HOST, PORT = "localhost", 23901

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

QUERIES = [
  "CGACCCCATGGACTGCAGCCACCAGGCTCCTCCATCCATGGGGTCGCTAAGAGTTGGACACGACTGAGAGACTTCACTTTCACTTTCCACTTTCATGCATT", 
  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 
  "CGACCCCATGGACTGCAGCCACCAGGCTCCTCCATCCATGGGGTCGCTAAGAGTTGGACACGACTGAGAGACTTCACTTTCACTTTCCACTTTCATGCATTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 
  "CGACCCCATGGACTGCAGCCACCAGGCTCCTCCATCCATGGGGTCGCTAAGAGTTGGACACGACTGAGAGACTTCACTTTCACTTTCCACTTTCATGCATT\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]

for index, query in enumerate(QUERIES):
    print("Send request {0}:".format(index))
    print(query)

    s.send(query)
    result = str(s.recv(4096))
    
    print("Got result:")
    print(result)