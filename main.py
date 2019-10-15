import os

my_net = '192.168.2.0/24'


def discover_IP_in_net():
    os.system('sudo apt install nmap -y')
    os.system('sudo nmap -sP ' + my_net)


def Install_centos_packages():
    os.system()


def Install_ubuntu_packages():
    ip = input('Enter your machine ip')
    os.system('ssh root@' + ip)

    #   --Python
    os.system('sudo apt update')
    os.system('sudo apt install software-properties-common -y')
    os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
    os.system('sudo apt install python3.7')

    #   --Docker
    os.system('sudo apt install apt-transport-https ca-certificates curl software-properties-common')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"')
    os.system('sudo apt update')
    os.system('apt-cache policy docker-ce')
    os.system('sudo apt install docker-ce -y')

    #   --Ansible
    print("Installing Ansible...")
    os.system('sudo apt update')
    os.system('sudo apt install software-properties-common')
    os.system('sudo apt-add-repository ppa:ansible/ansible')
    os.system('sudo apt update')
    os.system('sudo apt install ansible -y')

    # Net-tools
    print("Installing Net-Tools....")
    os.system('sudo apt-get install net-tools')

    # etc/hosts
    print("Update hosts file for Server...")
    os.system('sudo -- sh -c "echo 192.168.2.1 controller >> /etc/hosts"')
    os.system('sudo -- sh -c "echo 192.168.2.2 jenkins-master >> /etc/hosts"')

    # Change root password
    print("changing User Root Password...")
    os.system('sudo passwd root')

    # Snmp V3
    print("Installing Snmp.... ")
    os.system('sudo apt update')
    os.system('sudo apt install snmpd snmp libsnmp-dev -y')


def Install_jenkins():
    print()


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
        discover_IP_in_net()
    elif choice == 2:
        Install_centos_packages()
    elif choice == 3:
        Install_ubuntu_packages()
    elif choice == 4:
        Install_jenkins()
    elif choice == 5:
        return


spaces = "-=========~~~~~~=========-".center(100)

print("\n" + spaces)
print("--Main Script Controller--".center(100))
print(spaces + "\n")

main_menu()

while True:
    answer = input("Are you sure you want to leave, or go back to the main menu?\n1 = Main Menu\n2 = Leave")

    if answer == "2":
        break
    elif answer == "1":
        main_menu()
    else:
        print("Invalid input, try again.")
