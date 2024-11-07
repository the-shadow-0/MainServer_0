# MainServer_0
Linux Server Maintenance Script

Welcome to **MainServer_0**, a powerful and easy-to-use script designed for maintaining and securing Linux servers. This script automates common server maintenance tasks such as updating packages, securing SSH, configuring the firewall, and monitoring system resources. It is an all-in-one solution to keep your server healthy and secure.

## Features

- **System Updates**: Automatically updates packages and performs a distribution upgrade.
- **System Resource Usage**: Displays memory, disk, and CPU usage statistics.
- **Inode Usage**: Checks disk inode usage to ensure the system doesn't run out of inodes.
- **Log Monitoring**: Views the most recent system and authentication logs for potential issues.
- **Swappiness Optimization**: Optimizes swappiness settings for better performance.
- **SSH Hardening**: Secures SSH by changing the default port, disabling root login, and disabling password-based authentication.
- **Firewall Configuration**: Configures UFW to allow specific ports (SSH, HTTP, HTTPS).
- **Fail2Ban Installation**: Installs and configures Fail2Ban to protect against brute-force attacks.
- **AIDE Intrusion Detection**: Installs and initializes AIDE to monitor file integrity.
- **Disk Health Check**: Checks disk health using `fsck`.
- **MySQL Optimization**: Installs MySQLTuner and suggests optimizations (if MySQL is installed).

## Prerequisites

Before running this script, make sure that your Linux server meets the following requirements:

- **Root Access**: You need to run the script as root to perform administrative tasks.
- **Debian/Ubuntu-based OS**: This script is designed for Debian and Ubuntu distributions (uses `apt` for package management).
- **Python 3.x**: The script is written in Python 3.x.
  
## Installation

### 1. Download the Script

First, download the script to your server. You can either create the file manually or download it using `curl` or `wget`.

#### Option 1: Using `curl` to download
```bash
curl -o MainServer_0.py https://github.com/the-shadow-0/MainServer_0.git
```
#### Option 2: Using git clone to download
```bash
git clone https://github.com/the-shadow-0/MainServer_0.git
```
2. Set Permissions

Make sure the script has executable permissions. Run the following command:
```bash
chmod +x MainServer_0.py
```
3. Make It Executable (Optional)

If you want to execute the script directly like a shell command, you can move it to a directory in your PATH (e.g., /usr/local/bin/):
```bash
sudo mv MainServer_0.py /usr/local/bin/
```
You can now run the script by typing MainServer_0 in the terminal.
How to Run the Script

To execute the script, simply run the following command:
```bash
sudo python3 MainServer_0.py
```

Important Notes:

    The script must be run with root privileges (use sudo).
    The script is interactive, meaning it will display real-time updates about the tasks it is performing.

What the Script Does:

    Performs system updates (package and distribution upgrades).
    Displays system resource usage including memory, disk, and CPU statistics.
    Checks inode usage and warns if you're running low on inodes.
    Monitors logs for system and authentication errors or warnings.
    Optimizes swappiness for better memory management.
    Secures SSH:
        Changes SSH port to 2222.
        Disables root login.
        Disables password-based authentication.
    Configures UFW firewall to allow necessary ports (2222 for SSH, 80 for HTTP, 443 for HTTPS).
    Installs and configures Fail2Ban to prevent brute-force attacks.
    Installs and configures AIDE for file integrity monitoring.
    Runs a disk health check (fsck) to ensure the filesystem is free from errors.
    Runs MySQLTuner (if MySQL is installed) to suggest performance optimizations for the database.

Customization
Change SSH Port:

By default, the script changes the SSH port from 22 to 2222. If you wish to modify the port, simply edit the script and change the line:

file.write("Port 2222\n")

Replace 2222 with your preferred port number.
Disable/Enable Services:

The script does not disable any services by default.

Troubleshooting :

    Permission Denied: Make sure you're running the script with sudo (root access).
    Package Installation Issues: Ensure your server has access to the internet and the package repositories are up-to-date (apt update).
    Firewall Blocking SSH: If you cannot access your server after changing the SSH port, ensure you have allowed the new port through UFW.

Future Updates

This script will continue to evolve with additional features for system maintenance, monitoring, and security. If you'd like to contribute, feel free to submit a pull request or open an issue.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Developed by: the_shadow_0
Version: 1.0
Date: September 2024


### Explanation of Sections:

- **Introduction**: Provides a description of the script and its features.
- **Prerequisites**: Describes the required environment and dependencies (root access, Debian/Ubuntu OS).
- **Installation**: Step-by-step guide on how to download, set permissions, and execute the script.
- **How to Run the Script**: Explains how to run the script, the expected output, and the tasks the script performs.
- **Customization**: Instructions on how to customize SSH port and disable/enable services as per user requirements.
- **Troubleshooting**: Common issues and their solutions when running the script.
- **Future Updates**: Information on how the script will be updated in the future.
- **License**: Specifies the license under which the script is released (MIT License).

This `README.md` provides comprehensive instructions to help users understand the purpose, inst
