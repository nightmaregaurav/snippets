# SSH Port Forwarding

## Local Port Forwarding

Local port forwarding is used to access a service in or from your local machine that will be handled through a remote server. This is particularly useful when you want to securely access a service on a remote server as if it were running locally.

### Command Syntax:

```bash
ssh -o TCPKeepAlive=yes -o ExitOnForwardFailure=yes -N -f -L [local_port]:[remote_host]:[remote_port] [ssh_server]
```

#### Flags and Options:

- `-o TCPKeepAlive=yes`: Enables TCP keep-alive to ensure idle connections are not closed.
- `-o ExitOnForwardFailure=yes`: Terminates the SSH session if port forwarding fails.
- `-N`: Prevents the execution of remote commands after establishing the SSH connection.
- `-f`: Runs SSH in the background.
- `-L [local_port]:[remote_host]:[remote_port]`: Defines the local port forwarding rule.
  - `[local_port]`: The port on your local machine.
  - `[remote_host]`: The IP address or hostname of the remote server.
  - `[remote_port]`: The port on the remote server.

### Example:

Forward local port 8080 to a web server on a remote server:

```bash
ssh -o TCPKeepAlive=yes -o ExitOnForwardFailure=yes -N -f -L 8080:localhost:80 user@remote_server
```

After running this command, you can access the remote web server by opening a web browser and navigating to `http://localhost:8080`.

## Remote Port Forwarding

Remote port forwarding allows you to access a service in or from a remote server that will be handled through your local machine or another remote server. It's useful for exposing services running on remote servers to the local network or other remote servers.

### Command Syntax:

```bash
ssh -o TCPKeepAlive=yes -o ExitOnForwardFailure=yes -N -f -R [remote_port]:[local_host]:[local_port] [ssh_server]
```

#### Flags and Options:

- `-o TCPKeepAlive=yes`: Enables TCP keep-alive to ensure idle connections are not closed.
- `-o ExitOnForwardFailure=yes`: Terminates the SSH session if port forwarding fails.
- `-N`: Prevents the execution of remote commands after establishing the SSH connection.
- `-f`: Runs SSH in the background.
- `-R [remote_port]:[local_host]:[local_port]`: Defines the remote port forwarding rule.
  - `[remote_port]`: The port on the remote server.
  - `[local_host]`: The IP address or hostname of your local machine or another remote server.
  - `[local_port]`: The port on your local machine or the specified remote server.
