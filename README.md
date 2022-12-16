# Valstro Exercise

This repository contains the solution to the problem using python 3.9
Can be executed either from the cmd line or from docker.

## Execution from Cmd Line

Requires `Python 3.9` and the installation of thelibrary `python-socketio`:
```
pip install "python-socketio[client]"
```

The application allows to override the default connection: `0.0.0.0:3000`

### Using the defaults
Just start the application using this command:
```
python3.9 app.py
```

### Overriding host and port
If we want to override the host and port, start the application with
the following parameters:
```
python3.9  app.py --host 0.0.0.0 --port 3000
```

* --host: IP of the server
* --port: Port used by server

**Note**: It's not required to override both parameters, we can override the one desired.

## Execution from Docker

To make easier the execution, we have dockerized the Client implementation.
If the server is running from Docker, check the container IP address:

**Note**: Replace `server_container_name` by the name of the container of your Server app. 

```
docker inspect -f '' server_container_name
```

The previous command returns a lot of information but we're interested only with the **IPAddress**:

```
...
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "c343406bb7ab643b4953f95b50109d892a129a91472c1b845a04b1b0df06af2f",
                    "EndpointID": "8f1eae7aeb8f2bbaf9d9df2c57312d77d6b74f5f56efe87d9a86369ec4cb523f",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
...
```

Let's build and run the docker with the Client implementation.
```
docker build -t valstro .
docker run -it --rm --init -e "HOST=172.17.0.2" -e "PORT=3000" valstro
```

**Note**: Replace HOST ip by the one used by the server. (in our example `172.17.0.2`, returned by the inspect command)

## How to kill the Application

In both cases with `Control+C` the application will exit. If it takes sometime just click enter after `Control+C`

## References

* Python Socket-IO: https://python-socketio.readthedocs.io/en/latest/client.html
* Socket-IO v4: https://socket.io/docs/v4/
