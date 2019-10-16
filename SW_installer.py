import customed_ssh_client
import os;

user = 'moshe1'
password = 'root'


class Installer:

    def display_ips(self):
        print("\nFunction: display_ips()\n")

    def install_sw(self, ip):
        print(f"\nFunction: install_sw() on IP: {ip}\n")
        ssh_client = customed_ssh_client.CustomedSshClient(ip)
        ret_val = ssh_client.sendCommand('pwd')
        print(f"Returned Value:{ret_val}")
        ret_val = ssh_client.sendCommand('uname -r')
        print(f"Returned Value:{ret_val}")
        ssh_client.closeCconnection()
