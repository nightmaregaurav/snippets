``` bash
# replace /dev/sda with your device. install ovmf package from package manager if it's not found
sudo qemu-system-x86_64 -enable-kvm -m 8G -boot order=c -device usb-ehci -device usb-storage,drive=usbdisk -drive id=usbdisk,file=/dev/sda,format=raw,if=none -vga virtio -cpu host -smp 2 -bios /usr/share/OVMF/OVMF_CODE.fd -net nic -net user
```

OR use virt-manager (Enable XML editing first)

Create new VM >
Choose Manual install >
Select os type >
Set up resources >
Uncheck Enable Storage>
Check custimize before install >
Navigate to XML >
Add this to the device block:
``` xml
<controller type='usb' model='ehci'/>

<disk type='block' device='disk'>
  <driver name='qemu' type='raw'/>
  <source dev='/dev/sda'/>
  <target dev='sda' bus='usb'/>
  <address type='usb' bus='0' port='1'/>
</disk>
```
Apply but do not install
Change bios from overview to `......../OVMF/OVMF_CODE.fd` one
Click begin installation
