import os
import SW_installer


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
        SW_installer.Installer.display_ips()
    elif choice == 2:
        SW_installer.Installer.Install_centos_packages()
    elif choice == 3:
        SW_installer.Installer.install_ubuntu()
    elif choice == 4:
        Install_jenkins()
    elif choice == 5:
        return


spaces = "-=========~~~~~~=========-".center(100)

print("\n" + spaces)
print("--Main Script Controller--".center(100))
print(spaces + "\n")

installer = SW_installer.Installer()
main_menu()

while True:
    answer = input("Are you sure you want to leave, or go back to the main menu?\n1 = Main Menu\n2 = Leave")

    if answer == "2":
        break
    elif answer == "1":
        main_menu()
    else:
        print("Invalid input, try again.")
