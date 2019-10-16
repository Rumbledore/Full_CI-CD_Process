import customed_ssh_client
import os;

user = 'moshe1'
password = 'root'
my_net = '192.168.2.0/24'


class Installer:

    def __init__(self):
        self.ip = None
        self.ssh_client = None

    def display_ips(self):
        print("\nFunction: display_ips()\n")
        os.system('sudo apt install nmap -y')
        os.system('sudo nmap -sP ' + my_net)

    def install_sw(self, ip):
        self.ip = ip
        self.ssh_client = customed_ssh_client.CustomedSshClient(ip)
        print(f"\nFunction: install_sw() on IP: {self.ip}\n")
        self.install_ubuntu()
        # ssh_client = customed_ssh_client.CustomedSshClient(ip)
        # ret_val = ssh_client.sendCommand('pwd')
        # print(f"Returned Value:{ret_val}")
        # ret_val = ssh_client.sendCommand('uname -r')
        # print(f"Returned Value:{ret_val}")
        # ssh_client.closeCconnection()

    def install_ubuntu(self):
        # Python
        print("Installing Python....")  ##1
        ret_val = self.ssh_client.sendCommand('sudo apt update')
        ret_val = self.ssh_client.sendCommand('sudo apt install software-properties-common -y')
        ret_val = self.ssh_client.sendCommand('sudo add-apt-repository ppa:deadsnakes/ppa -y')
        ret_val = self.ssh_client.sendCommand('sudo apt install python3.7 -y')
        ret_val = self.ssh_client.sendCommand('python3.7 --version')
        print("\n FINISH Python Installation! =]")

        # Docker
        print("\nInstalling Docker....")  ##2
        ret_val = self.ssh_client.sendCommand('sudo apt update')
        ret_val = self.ssh_client.sendCommand(
            'sudo apt install apt-transport-https ca-certificates curl software-properties-common')
        ret_val = self.ssh_client.sendCommand(
            'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
        ret_val = self.ssh_client.sendCommand(
            'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"')
        ret_val = self.ssh_client.sendCommand('sudo apt update')
        ret_val = self.ssh_client.sendCommand('apt-cache policy docker-ce')
        ret_val = self.ssh_client.sendCommand('sudo apt install docker-ce -y')
        print("\n FINISH Docker Installation! =]")

        # Ansible
        print("\nInstalling Ansible...")  ##3
        ret_val = self.ssh_client.sendCommand('sudo apt update')
        ret_val = self.ssh_client.sendCommand('sudo apt install software-properties-common -y')
        ret_val = self.ssh_client.sendCommand('sudo apt-add-repository ppa:ansible/ansible -y')
        ret_val = self.ssh_client.sendCommand('sudo apt update')
        ret_val = self.ssh_client.sendCommand('sudo apt install ansible -y')
        print("\n FINISH Ansible Installation! =]")

        # Net-tools
        print("\nInstalling Net-Tools....")  ##4
        ret_val = self.ssh_client.sendCommand('sudo apt-get install net-tools')
        print("\n FINISH Net-tools Installation! =]")

        # # etc/hosts
        # print("\nUpdate hosts file for Server...")  ##5
        # ret_val = self.ssh_client.sendCommand('sudo -- sh -c "echo 192.168.2.104 controller >> /etc/hosts"')
        # ret_val = self.ssh_client.sendCommand('sudo -- sh -c "echo 192.168.2.105 jenkins-master >> /etc/hosts"')
        # print("\n FINISH etc/hosts Configuration! =]")

        # Change root password
        print("\nChanging User Root Password...")  ##6
        ret_val = self.ssh_client.sendCommand('sudo passwd root')
        print("\n FINISH Change root password! =]")

        # Snmp V3
        print("\nInstalling Snmp.... ")  ##7
        ret_val = self.ssh_client.sendCommand('sudo apt update')
        ret_val = self.ssh_client.sendCommand('sudo apt install snmpd snmp libsnmp-dev -y')
        print("\n FINISH Snmp V3 Installation! =]")

    def Install_centos_packages(self):
        print()
        #   --Python
        # print('Installing python...')
        # os.system('sudo yum install centos-release-scl')
        # os.system('sudo yum -y install rh-python37')
        # os.system('scl enable rh-python37 bash')
        #
        # #   --Docker
        # print('Installing docker...')
        # os.system('sudo yum update')
        # os.system('sudo yum install yum-utils device-mapper-persistent-data lvm2')
        # os.system('sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
        # os.system('sudo yum -y install docker-ce')
        # os.system('sudo systemctl start docker')
        # os.system('sudo systemctl enable docker')
        #
        # #   --Ansible
        # print("Installing Ansible...")
        # os.system('sudo yum install epel-release')
        # os.system('sudo -y yum install ansible')
        #
        # # Net-tools
        # print("Installing Net-Tools....")
        # os.system('yum -y install net-tools')
        #
        # # etc/hosts
        # print("Update hosts file for Server...")
        # os.system('sudo -- sh -c "echo 192.168.2.1 controller >> /etc/hosts"')
        # os.system('sudo -- sh -c "echo 192.168.2.2 jenkins-master >> /etc/hosts"')
        #
        # # Change root password
        # print("changing User Root Password...")
        # os.system('sudo passwd root')
        #
        # # Snmp V3
        # print("Installing Snmp.... ")
        # os.system('yum -y install net-snmp net-snmp-utils')
