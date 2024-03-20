import subprocess
import itertools

target_ip = input("Enter IP: ")
knocking = ["066", "666", "3432"]

def port_knocking(target_ip, port_combination):
    for port in port_combination:
        nmap = f"sudo nmap -Pn --max-retries 0 -p {','.join(port)} {target_ip}"
        subprocess.run(nmap, shell=True)
        print(nmap)

def main():
    port_permutation = itertools.permutations(knocking)
    for permutation in port_permutation:
        port_knocking(target_ip, [permutation])
    print("Port knocking completed.")

if __name__ == "__main__":
    main()
