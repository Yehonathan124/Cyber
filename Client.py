# Client
import socket
import os

HOST = 1234  # The server's hostname or IP address
PORT = 65432        # The port used by the server

BUFFER_SIZE = 1024

def upload_file(filename):
    """
    Uploads a file to the server.
    """
    # Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: File {filename} not found.")
        return

    # Get file size
    filesize = os.path.getsize(filename)

    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    # Send filename
    sock.sendall(filename.encode())

    # Receive server response
    response = sock.recv(BUFFER_SIZE).decode()

    if response.startswith("ERR"):
        print(response)
        return sock.close()
        

    # Send file data
    with open(filename, "rb") as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            sock.sendall(data)

    # Receive upload confirmation
    response = sock.recv(BUFFER_SIZE).decode()
    print(response)

    sock.close()

def main():
    """
    Main function to prompt user for filename and upload the file.
    """
    filename = input("Enter filename to upload: ")
    upload_file(filename)

if __name__ == "__main__":
  main()