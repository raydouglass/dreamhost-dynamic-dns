# Dynamic DNS for Dreamhost

A simple script and Dockerfile to dynamically update a DNS record on a [Dreamhost](https://www.dreamhost.com/) account.

## Setup

Get an [API key](https://help.dreamhost.com/hc/en-us/articles/4407354972692-Connecting-to-the-DreamHost-API) from Dreamhost [here](https://panel.dreamhost.com/?tree=home.api) with `All dns functions` allowed

## Running

### Standalone

You can run the script standalone if you have `requests` installed:
```
env API_KEY=<dreamhost_api_key> DOMAIN=<my_domain.com> python update_dns.py
```

### Docker

You can run the script in a docker container:
```
docker run -it --rm \
    -e API_KEY=<dreamhost_api_key> \
    -e DOMAIN=<my_domain.com>
    raydouglass/dreamhost-dynamicdns:latest
```

## Configuration

There are two required and on optional environment variables:
- `API_KEY` - An API key from Dreamhost with `All dns functions` allowed
- `DOMAIN` - A comma separated list of domain names that have DNS enabled on the Dreamhost account
- `IP_LOOKUP_URL` - Optional: a URL which returns the IP address of the user as plain text
  - By default this is https://api.ipify.org/?format=text
  - Another one could be https://wtfismyip.com/text
