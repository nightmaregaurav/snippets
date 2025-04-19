## Install and configure SSL/TLS certificate for ASP.NET Core application

### Install certutil and create NSS database

To install certutil, run the following command:

```bash
sudo apt-get install libnss3-tools
sudo dnf install nss-tools
```

Then, create a new NSS database:

```bash
mkdir -p $HOME/.pki/nssdb
certutil -d $HOME/.pki/nssdb -N
```

### Generate and install a new development certificate

First, remove any existing development certificate:

```bash
dotnet dev-certs https --clean
```

Then, generate a new development certificate:

```bash
sudo mkdir -p /usr/local/share/ca-certificates/aspnet/
dotnet dev-certs https
sudo dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
```

### Trust the new certificate

To trust the new certificate, run the following commands:

```bash
sudo certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n localhost -i /usr/local/share/ca-certificates/aspnet/https.crt
sudo certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n localhost -i /usr/local/share/ca-certificates/aspnet/https.crt
```

### Configure Firefox to trust the new certificate

To configure Firefox to trust the new certificate, run the following command:

```bash
firefox_lib_folder=/usr/lib/firefox
sudo mkdir -p $firefox_lib_folder
sudo touch $firefox_lib_folder/distribution/policies.json
cat <<EOF | sudo tee $firefox_lib_folder/distribution/policies.json
{
    "policies": {
        "Certificates": {
            "Install": [
                "/usr/local/share/ca-certificates/aspnet/https.crt"
            ]
        }
    }
}
EOF
```

### Update the CA trust

Finally, update the CA trust:

```bash
sudo update-ca-trust
sudo trust extract-compat
```

After following these steps, your ASP.NET Core application should be accessible over HTTPS using the newly installed certificate.
