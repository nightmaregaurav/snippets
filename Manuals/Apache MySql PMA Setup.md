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
``` bash
sudo pacman -S phpmyadmin
```

# Configure phpMyAdmin
``` bash
sudo nano /etc/httpd/conf/extra/phpmyadmin.conf
```
# Add these lines:
    Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
    <Directory "/usr/share/webapps/phpMyAdmin">
        DirectoryIndex index.php
        AllowOverride All
        Options FollowSymlinks
        Require all granted
    </Directory>
    
# Configure Permission
``` bash
sudo chmod 644 /etc/httpd/conf/extra/phpmyadmin.conf
```

# Add the phpMyAdmin configuration to httpd.conf
``` bash
sudo nano /etc/httpd/conf/httpd.conf
```
# Add this line at the end:
    Include conf/extra/phpmyadmin.conf

# Create a temporary directory for phpMyAdmin
``` bash
sudo mkdir -p /var/lib/phpmyadmin/tmp
sudo chown -R http:http /var/lib/phpmyadmin/tmp
```

# Configure phpMyAdmin to use the temporary directory and a blowfish secret
``` bash
sudo mkdir /etc/phpmyadmin
sudo cp /usr/share/webapps/phpMyAdmin/config.sample.inc.php /usr/share/webapps/phpMyAdmin/config.inc.php
sudo nano /usr/share/webapps/phpMyAdmin/config.inc.php
```
# Update these lines:
    $cfg['TempDir'] = '/var/lib/phpmyadmin/tmp';
    $cfg['blowfish_secret'] = 'replace with 32bit randomstrings';

# Enable the required PHP extensions
``` bash
sudo nano /etc/php/php.ini
```
# Uncomment these lines:
    extension=mysqli
    extension=curl
    extension=iconv

# Restart the Apache service
``` bash
sudo systemctl restart httpd.service
```
