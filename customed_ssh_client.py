import paramiko


class CustomedSshClient:

    ssh = paramiko.SSHClient()
    user = 'moshe1'
    password = 'root'

    def __init__(self, host_ip):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host_ip, username=self.user, password=self.password, look_for_keys=False)

    def sendCommand(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode('ascii').strip("\n")

    def closeCconnection(self):
        self.ssh.close()