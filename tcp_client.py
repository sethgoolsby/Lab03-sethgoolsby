"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"

Developer: Seth Goolsby
Student ID: 8504036914
GitHub Repository Link:  https://github.com/sethgoolsby/Lab03-sethgoolsby.git
"""
import socket

def main():
	HOST = '18.191.85.112'
	PORT = 5005
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
		mySocket.connect((HOST,PORT))
    # TODO: Get user input and send it to the server using your TCP socket
		userData = bytes(input("Enter what you want to send to the server"), 'utf-8')
		mySocket.sendall(userData)
 # TODO: Receive a response from the server and close the TCP connection
		serverData = mySocket.recv(1024)
	print("Recieved",repr(serverData))
if __name__ == '__main__':
	main()
