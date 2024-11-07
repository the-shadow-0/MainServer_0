#!/usr/bin/env python3

import os
import subprocess

def display_banner():
    banner =    "==================================================="
    banner += "\n              Welcome to MainServer_0              "
    banner += "\n     A Powerful Tool for Linux servers maintenance "
    banner += "\n                   Developed by the_shadow_0       "
    banner += "\n==================================================="
    print(banner)

def run_command(command, capture_output=False):
    """
    Run a shell command and optionally capture the output.
    :param command: The shell command to run.
    :param capture_output: Whether to capture and return the output or just print it.
    :return: Output of the command if capture_output=True, else None.
    """
    result = subprocess.run(command, shell=True, text=True, capture_output=capture_output)
    
    if capture_output:
        return result.stdout
    else:
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return result.returncode

display_banner()

if os.geteuid() != 0:
    print("Please run as root")
    exit(1)

print("Updating system packages...")
run_command("apt update && apt upgrade -y") 
run_command("apt dist-upgrade -y")  
print("System packages updated.")

print("\n---- System Resource Usage ----")
print("Memory Usage:")
run_command("free -h", capture_output=True)
print("Disk Usage:")
run_command("df -h", capture_output=True)
print("CPU Load:")
run_command("uptime", capture_output=True)

print("\nChecking Inode Usage...")
run_command("df -i", capture_output=True)

print("\n---- Recent Syslog Entries ----")
run_command("tail -n 20 /var/log/syslog", capture_output=True)

print("\n---- Recent Auth Log Entries ----")
run_command("tail -n 20 /var/log/auth.log", capture_output=True)

print("\nOptimizing swappiness...")
run_command("sysctl vm.swappiness=10")
with open('/etc/sysctl.conf', 'a') as sysctl_conf:
    sysctl_conf.write("\nvm.swappiness=10")
print("Swappiness set to 10.")

print("\nHardening SSH...")
sshd_config = "/etc/ssh/sshd_config"

with open(sshd_config, 'r') as file:
    ssh_config_data = file.readlines()

with open(sshd_config, 'w') as file:
    for line in ssh_config_data:
        if "#Port 22" in line:
            file.write("Port 2222\n")
        elif "PermitRootLogin yes" in line:
            file.write("PermitRootLogin no\n")
        elif "#PasswordAuthentication yes" in line:
            file.write("PasswordAuthentication no\n")
        else:
            file.write(line)

run_command("systemctl restart ssh")
print("SSH hardened (Port 2222, Root login disabled, PasswordAuthentication disabled).")

print("\nConfiguring UFW Firewall...")
run_command("ufw allow 2222/tcp")  
run_command("ufw allow 80/tcp") 
run_command("ufw allow 443/tcp") 
run_command("ufw enable") 
run_command("ufw status verbose")  
print("UFW firewall enabled and configured.")

print("\nInstalling and Configuring Fail2Ban...")
run_command("apt install fail2ban -y") 
run_command("systemctl enable fail2ban") 
run_command("systemctl start fail2ban")  
print("Fail2Ban installed and configured.")

print("\nInstalling and Configuring AIDE for intrusion detection...")
run_command("apt install aide -y") 
run_command("aideinit")  
run_command("cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db")
run_command("aide --check")
print("AIDE installed and initialized.")

print("\nPerforming disk health check...")
run_command("fsck -N /dev/sda1")  

if run_command("command -v mysql", capture_output=True):
    print("\nRunning MySQLTuner...")
    run_command("apt install mysqltuner -y")
    run_command("mysqltuner")


print("\nMaintenance script completed!")
