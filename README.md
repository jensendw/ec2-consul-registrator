# EC2 Consul Registrator

## Overview
This app queries AWS for amazon managed services and creates consul external services for them.

## Setup

See the docker-compose.yml for what environment variables need to be set, an explanation of each variable is noted below:

* CONSUL_URL
** The URL of the consul server
* AWS_ACCESS_KEY_ID
** AWS access key with the appropriate permissions
* AWS_SECRET_ACCESS_KEY
** AWS secret key with the appropriate permissions
* AWS_DEFAULT_REGION
** The AWS region you want to connect to


## Deployment

The easiest way to get started is by modifying your rancher-compose.yml file with the appropriate values, and then running:

```shell
docker-compose up
```

This will register the relevant external AWS services on your consul server.
