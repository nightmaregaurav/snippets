# Perform after a live boot

## Backup
``` bash
	sudo dd if=/dev/nvme0n1 conv=sync,noerror bs=2M status=progress | gzip -c | split -b 2000m - /run/media/liveuser/cb6710c1-3de3-4bb9-a13e-5cfd0acc3219/nvme0n1.bin.gz
```

## Restore
``` bash
	sudo cat /run/media/liveuser/cb6710c1-3de3-4bb9-a13e-5cfd0acc3219/nvme0n1.bin.gz.* | gzip -dc | dd of=/dev/sda conv=sync,noerror bs=2M status=progress
```