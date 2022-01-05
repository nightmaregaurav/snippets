#!/bin/sh

urls=(ifconfig.me icanhazip.com api.ipify.org ipinfo.io/ip ipecho.net/plain)

while [ 0 -lt 1 ]
do
	rand=$[$RANDOM % ${#urls[@]}]
	url=${urls[$rand]}
	command="curl -s $url"
	ip=$($command)
	datetime=$(date)
	data="{ 'Server used': '$url', 'Server command': '$command', 'Exact time': '$datetime', 'Device IP': '$ip' }"

	echo $data
done