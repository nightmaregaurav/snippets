# Remove zram swap
systemctl --type swap
sudo systemctl mask <name>-zram0.swap

# Set swapfile
sudo touch /swapfile
sudo chattr +C /swapfile
sudo fallocate -l 48G /swapfile
sudo chmod 600 /swapfile
sudo lsattr /swapfile  # make sure you see the letter C in the results: ---------------C------ /swapfile
sudo mkswap /swapfile  # Setting up swapspace version 1, size = 48 GiB...
sudo swapon /swapfile
sudo nano /etc/fstab 
	- Write: `/swapfile swap swap defaults 0 0`
sudo swapon -s
