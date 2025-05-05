import socket

target = "scanme.nmap.org" 
ports = [21, 22, 80, 443, 3306] 
print(f"Scanning {target}...\n")

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(1)  
        result = sock.connect_ex((target, port)) 
        if result == 0:
            print(f"Port {port} is OPEN")  
        else:
            print(f"Port {port} is CLOSED")  
        sock.close()  
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
