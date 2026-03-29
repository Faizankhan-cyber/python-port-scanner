import socket
start = int(input("Start port: "))
end = int(input("End port: "))
target = input("Enter target (IP or website): ")

for port in range(1, 101):

print(f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    
    s.close()
