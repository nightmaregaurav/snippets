# Install MariaDB and MariaDB clients From package manager
- Arch
``` bash
sudo pacman -S mariadb mariadb-clients
```
- RHEL
``` bash
sudo dnf install mariadb mariadb-server
```
- Debian
``` bash
sudo apt install mariadb mariadb-clients
```

# Initialize the MariaDB data directory
``` bash
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

# Enable and start the MariaDB service
``` bash
sudo systemctl enable --now mariadb.service
sudo systemctl start mariadb.service
```

# Upgrade the MariaDB system tables
``` bash
sudo mysql_upgrade --force
```

# Secure the MariaDB installation
``` bash
sudo mysql_secure_installation
```

# Create a new user 'pma' and grant privileges
``` bash
sudo mysql -u root -p
```
``` sql 
CREATE USER 'pma'@'localhost' identified by 'pma';
grant all on *.* to 'pma'@'localhost';
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED VIA mysql_native_password USING PASSWORD('');
commit;
exit;
```

# Install Apache, PHP, and PHP-Apache From package manager
- Arch
``` bash
sudo pacman -S httpd php
```
- RHEL
``` bash
sudo dnf install httpd php
```
- Debian
``` bash
sudo apt install httpd php
```

# Start the Apache service
``` bash
sudo systemctl start httpd.service
```

# Install phpMyAdmin
- Arch
``` bash
sudo pacman -S phpmyadmin
```
- RHEL
``` bash
sudo dnf install phpmyadmin
```
- Debian
``` bash
sudo apt install phpmyadmin
```

# Restart the Apache service
``` bash
sudo systemctl restart httpd.service
```
