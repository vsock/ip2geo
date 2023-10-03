# IP address to Geo location

Simple API to get geo location co-oridnates.

## Description

This command line uitility can be used to obtain the physical location of remote server.

## Getting Started

### Dependencies

python version 3.x.x
if using Docker version 24.0.6 

### Installing & Running on Linux/Mac

* Clone this repository to your pc (linux/mac) 

### Build and Run with Docker 
* cd ~/\<repo>
* docker build --tag ip2geo_latest
* docker run ip2geo_vs \<ip_address>
 
e.g on debian
```
$ sudo docker run ip2geo_vs 142.250.200.36
```
```
$ sudo docker run ip2geo_vs www.google.com
```
### Build & Run from source code
* pip install -r requirements.txt
* python3 ip2geo.py <Domain_name>/<ipv4>/<ipv6>
```
python3 ip2geo.py www.google.com 
```
```
python3 ip2geo.py 172.217.18.4
```
```
python3 ip2geo.py 0000:0000:0000:0000:0000:ffff:d8ef:2678
```

### Installing & Running on Windows

* clone this repository to Windows PC
* simply run python3 ip2geo.py ip_address
* follow the docker windows image build & run instruction from here:
* https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-docker/manage-windows-dockerfile


## Help

```
-h on the tool will provide the following

usage: IP to GEO LOCATION [-h] [-v] ip_address

script prints GEO location coordinates in latittude,longitude format for a
given TCP/IP address

positional arguments:
  ip_address     Enter a valid ip address or url i.e 142.251.46.228 or
                 www.google.com

options:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
```

## Authors

Contributors names and contact info

Vairavan Sockalingam

## Version History

* 0.1
    * Initial Release
