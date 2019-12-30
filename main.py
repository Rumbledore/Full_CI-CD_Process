import paramiko
import os

user = 'root'
password = 'root'
my_net = '192.168.1.29/24'


class CustomedSshClient:

    ssh = paramiko.SSHClient()

    def __init__(self, host_ip):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host_ip, username=user, password=password, look_for_keys=False)

    def sendCommand(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        exit_status = stdout.channel.recv_exit_status()
        if exit_status == 0:
            print("Command Succeeded!")
        print(stdout.read().decode('ascii').strip("\n"))
        return stdout.read().decode('ascii').strip("\n")

    def closeCconnection(self):
        self.ssh.close()


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
        self.ssh_client = CustomedSshClient(ip)
        print(f"\nFunction: install_sw() on IP: {self.ip}\n")
        # self.install_ubuntu()
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

    #TODO
    def install_centos(self):
        # Python 3.7

        print("Installing Python....")
        os.system('yum install gcc openssl-devel bzip2-devel libffi-devel')
        os.system('cd /usr/src')
        os.system('wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz')
        os.system('tar xzf Python-3.7.4.tgz')
        os.system('cd Python-3.7.4')
        os.system('./configure --enable-optimizations')
        os.system('make altinstall')
        os.system('rm /usr/src/Python-3.7.4.tgz')
        os.system('python3.7 -V')
        # Docker
        print("Installing Docker....")
        os.system('sudo yum install -y yum-utils \
                      device-mapper-persistent-data \
                      lvm2')
        os.system('sudo yum-config-manager \
                      --add-repo \
                      https://download.docker.com/linux/centos/docker-ce.repo')
        os.system('sudo yum install -y docker-ce docker-ce-cli containerd.io')
        os.system('sudo systemctl start docker')

        # Ansibale

        print("Installing Ansibale....")
        os.system('yum install epel-release -y')
        os.system('yum install ansible')
        os.system('ansible --version')

        # Net-tools
        print("Installing Net-Tools....")
        os.system('yum install -y net-tools')

        # etc/hosts
        print("Update hosts file for Server...")
        os.system('echo 192.168.2.1 controller >> /etc/hosts"')
        os.system('echo 192.168.2.2 jenkins-master >> /etc/hosts"')

        # Change root password
        print("changing User Root Password...")
        os.system('sudo passwd root')

        # Snmp V3
        print("Installing Snmp.... ")
        os.system('yum -y install net-snmp net-snmp-utils')

        # Installation not check on centos7!!!!!

    def install_jenkins(self):
        print('installing jenkins')
        is_master = input('Enter M for "master"/ "S" for slave')
        if is_master == "M":
            ret_val = self.ssh_client.sendCommand('sudo apt update')
            ret_val = self.ssh_client.sendCommand('sudo apt install openjdk-8-jdk')
            ret_val = self.ssh_client.sendCommand(
                'wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -')
            ret_val = self.ssh_client.sendCommand(
                "sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
            ret_val = self.ssh_client.sendCommand("sudo apt update")
            ret_val = self.ssh_client.sendCommand("sudo apt install jenkins")
        elif is_master == "S":
            ret_val = self.ssh_client.sendCommand('sudo apt update')
            ret_val = self.ssh_client.sendCommand('sudo apt install openjdk-8-jdk')
            ret_val = self.ssh_client.sendCommand(
                'wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -')
            ret_val = self.ssh_client.sendCommand(
                "sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
        print("\n FINISH Jenkins Installation! =]")


def enter_ip():
    ip_input = False
    while not ip_input:
        ip_str = input("Enter IP address for Installation:")
        ip_parse_str = str(ip_str)
        octets_list = ip_parse_str.split(".")
        if len(octets_list) != 4:
            print("IP address  - Wrong Format  -  Should contain 4 octets")
            continue
        for i in range(4):
            octet_as_num = int(octets_list[i])
            if octet_as_num < 0 or octet_as_num > 255:
                print("Aborting - octets value should be between 0 and 255")
                break
            else:
                if i == 3:
                    ip_input = True
    return ip_str


def menu_text():
    print("Main Menu:".center(100))
    print("1.Discover all IP's in net".center(100))
    print("2.Install full packages centos".center(104))
    print("3.Install full packages ubuntu".center(104))
    print("4.Install jenkins M&S".center(96))
    print("5.Leave".center(82))


def main_menu():
    menu_text()
    choice = int(input())
    if choice == 1:
        installer.display_ips()
    elif choice == 2:
        installer.install_sw(enter_ip())
        installer.install_centos()
    elif choice == 3:
        installer.install_sw(enter_ip())
        installer.install_ubuntu()
    elif choice == 4:
        installer.install_jenkins()
    elif choice == 5:
        return


# Main

spaces = "-=========~~~~~~=========-".center(100)
print("\n" + spaces)
print("--Main Script Controller--".center(100))
print(spaces + "\n")

installer = Installer()
main_menu()

while True:
    answer = input("Are you sure you want to leave, or go back to the main menu?\n1 = Main Menu\n2 = Leave")

    if answer == "2":
        break
    elif answer == "1":
        main_menu()
    else:
        print("Invalid input, try again.")
