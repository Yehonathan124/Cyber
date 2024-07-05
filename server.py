# server 

import socket
import os

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024

# Define the upload directory on the server
UPLOAD_DIR = "D:\""
def handle_client(conn, addr):
  """
  Handles a client connection for uploading a file.
  """
  print(f"Connected by {addr}")

  # Receive filename
  filename = conn.recv(BUFFER_SIZE).decode()

  # Check if filename is valid
  if not filename or os.path.sep in filename:
    conn.sendall("ERR: Invalid filename".encode())
    return

  # Create upload path
  upload_path = os.path.join(UPLOAD_DIR, filename)

  # Check if directory exists, create it if not
  if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

  # Receive file data
  with open(upload_path, "wb") as f:
    while True:
      data = conn.recv(BUFFER_SIZE)
      if not data:
        break
      f.write(data)

  print(f"File {filename} uploaded from {addr}")
  conn.sendall("OK: Upload successful".encode())

  conn.close()

def main():
  """
  Main function to start the server.
  """
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((HOST, PORT))
  sock.listen()

  print(f"Server listening on {HOST}:{PORT}")

  while True:
    conn, addr = sock.accept()
    handle_client(conn, addr)

if __name__ == "__main__":
  main()