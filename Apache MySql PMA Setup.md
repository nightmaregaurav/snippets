# Install MariaDB and MariaDB clients
    sudo pacman -S mariadb mariadb-clients

# Initialize the MariaDB data directory
    sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

# Enable and start the MariaDB service
    sudo systemctl enable --now mariadb.service
    sudo systemctl start mariadb.service

# Upgrade the MariaDB system tables
    sudo mysql_upgrade --force

# Secure the MariaDB installation
    sudo mysql_secure_installation

# Create a new user 'pma' and grant privileges
    sudo mysql -u root -p
    CREATE USER 'pma'@'localhost' identified by 'pma';
    grant all on *.* to 'pma'@'localhost';
    FLUSH PRIVILEGES;
    ALTER USER 'root'@'localhost' IDENTIFIED VIA mysql_native_password USING PASSWORD('');
    commit;
    exit;

# Install Apache, PHP, and PHP-Apache
    sudo pacman -S apache php php-apache

# Configure Apache to use PHP
    sudo nano /etc/httpd/conf/httpd.conf
# Comment the line:
    LoadModule mpm_event_module modules/mod_mpm_event.so
# Uncomment the line:
    LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
# Add this line at the end of the LoadModule list: 
    LoadModule php_module modules/libphp.so
    AddHandler php-script .php
# Add this line at the end of the Include list: 
    Include conf/extra/php_module.conf

# Enable and start the Apache service
    sudo systemctl enable --now httpd.service
    sudo systemctl start httpd.service

# Install phpMyAdmin
    sudo pacman -S phpmyadmin

# Configure phpMyAdmin
    sudo nano /etc/httpd/conf/extra/phpmyadmin.conf
# Add these lines:
    Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
    <Directory "/usr/share/webapps/phpMyAdmin">
        DirectoryIndex index.php
        AllowOverride All
        Options FollowSymlinks
        Require all granted
    </Directory>
    
# Configure Permission
    sudo chmod 644 /etc/httpd/conf/extra/phpmyadmin.conf

# Add the phpMyAdmin configuration to httpd.conf
    sudo nano /etc/httpd/conf/httpd.conf
# Add this line at the end:
    Include conf/extra/phpmyadmin.conf

# Create a temporary directory for phpMyAdmin
    sudo mkdir -p /var/lib/phpmyadmin/tmp
    sudo chown -R http:http /var/lib/phpmyadmin/tmp

# Configure phpMyAdmin to use the temporary directory and a blowfish secret
    sudo mkdir /etc/phpmyadmin
    sudo cp /usr/share/webapps/phpMyAdmin/config.sample.inc.php /usr/share/webapps/phpMyAdmin/config.inc.php
    sudo nano /usr/share/webapps/phpMyAdmin/config.inc.php
# Update these lines:
    $cfg['TempDir'] = '/var/lib/phpmyadmin/tmp';
    $cfg['blowfish_secret'] = 'replace with 32bit randomstrings';

# Enable the required PHP extensions
    sudo nano /etc/php/php.ini
# Uncomment these lines:
    extension=mysqli
    extension=curl
    extension=iconv

# Restart the Apache service
    sudo systemctl restart httpd.service
