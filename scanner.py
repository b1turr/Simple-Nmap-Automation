import nmap

# Initialize the scanner
scanner = nmap.PortScanner()

print("--- Simple Nmap Scanner ---")
target_ip = input("Enter the IP to scan: ")

print(f"Scanning {target_ip}... Please wait.")

# I'm using -sV to get service versions.
# Scanning only ports 1-1000 to keep it fast.
try:
    scanner.scan(target_ip, arguments='-sV -p 1-1000')
except Exception as e:
    print(f"Error: {e}")
    exit()

# Save results to a file
output_file = "scan_results.txt"

with open(output_file, "w") as f:
    f.write(f"Scan Report for: {target_ip}\n")
    f.write("-" * 30 + "\n")

    # Check if host is actually found
    if target_ip in scanner.all_hosts():
        
        # Loop through protocols (TCP/UDP)
        for proto in scanner[target_ip].all_protocols():
            f.write(f"\nProtocol: {proto}\n")
            
            # Get all open ports
            ports = scanner[target_ip][proto].keys()
            
            for port in sorted(ports):
                state = scanner[target_ip][proto][port]['state']
                service = scanner[target_ip][proto][port]['name']
                
                # Write to file (Format: Port - State - Service)
                f.write(f"Port: {port}\tState: {state}\tService: {service}\n")
                
        print(f"Success! Report saved to {output_file}")
        
    else:
        print("Host seems down or blocked.")