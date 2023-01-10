# get Pem CA CERT
openssl pkcs12 -in *.pfx -out *.pem -cacerts -nokeys

# get Pem CLIENT CERT
openssl pkcs12 -in *.pfx -out *.pem -clcerts -nokeys

# get Pem PRIV KEY
openssl pkcs12 -in *.pfx -nocerts -nodes | openssl rsa -out *.pem

# Convert PFX to PEM
openssl pkcs12 -nodes -in *.pfx -out *.pem