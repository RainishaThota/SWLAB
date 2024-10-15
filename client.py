import socket
import sys

def start_client(server_ip, server_port):
    """
    Starts the client, connects to the server, sends arithmetic expressions to the server,
    and receives the evaluated result back from the server.
    """
    # Create a TCP socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server using the provided IP and port
        client.connect((server_ip, server_port))
        print(f"Connected to server {server_ip}:{server_port}")

        try:
            # Enter a loop to continuously send expressions to the server
            while True:
                # Get the arithmetic expression from the user
                expression = input("Enter an arithmetic expression (e.g., 3 + 4): ")

                # Send the expression to the server, encoding it into bytes
                client.send(expression.encode())

                # Receive the result from the server, decoding it back into a string
                result = client.recv(1024).decode()
                
                # Print the result received from the server
                print(f"Result from server: {result}")

        except KeyboardInterrupt:
            # Handle the case where the user interrupts the program (Ctrl+C)
            print("\nClient terminated.")
    except Exception as e:
        # Handle any connection errors (e.g., server not available)
        print(f"Connection error: {e}")
        sys.exit(1)
    finally:
        # When the client exits, ensure the socket is closed
        print("\nDisconnected from server.")
        client.close()

if __name__ == "__main__":
    # Ensure that the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    # Get the server IP and port from the command-line arguments
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    # Start the client and connect to the specified server
    start_client(server_ip, server_port)

