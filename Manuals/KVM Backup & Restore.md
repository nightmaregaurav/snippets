# Backup
``` bash
	cd /var/lib/libvirt/images
	sudo -i
	virsh dumpxml <<vm-name>> > <<vm-name>>.xml
	mkdir <<vm-name>>
	mv <<vm-name>>.xml <<vm-name>>
	cp <<vm-name>>.qcow2 <<vm-name>>
	tar -cvfp <<vm-name>>-qemu.tar <<vm-name>>
	mv <<vm-name>>-qemu.tar.bz2 ~/destination
```

# Restore
``` bash
	tar -xvfp <<vm-name>>-qemu.tar
	cd <<vm-name>>
	sudo -i
	virsh define --file <<vm-name>>.xml
	mv <<vm-name>>.qcow2 /var/lib/libvirt/images/
```