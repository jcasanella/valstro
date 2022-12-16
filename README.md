# Valstro Exercise

This repository contains the solution to the problem using python 3.9
It can be executed from host or from docker.

## Execution from Host

Requires `Python 3.9` and the installation of the following library:
```
pip install "python-socketio[client]"
```

Once the library is installed the application can use the default `hostname:port`. In this case will 
connect against: `0.0.0.0:3000`

To start the application run:
```
python3.9 app.py
```

If we want to override the default host and port, start the application with
the parameters to override the host and port:
```
python3.9  app.py --host 0.0.0.0 --port 3000
```

**Note**: If you want to override just one parameter, supply only the parameter to override.

## Execution from Docker

If the server is running from Docker, check the container IP address:
```
docker inspect -f '' server_container_name
```
**Note**: You must replace `server_container_name` by the name of the container of your Server app. 

The inspect command returns a lot of information:

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

However, We're only interested with the **IPAddress** value. In our example is `172.17.0.2` 

Let's build and run the docker with the client implementation.
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