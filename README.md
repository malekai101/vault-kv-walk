# Vault KV Walk

## Overview

This a simple python program to list accounts stored in a HashiCorp KV store without the calling code being authorized to read password data.  This demo code to show off two Vault endpoints:

* The read secrets subkeys [endpoint](https://developer.hashicorp.com/vault/api-docs/secret/kv/kv-v2#read-secret-subkeys)
* The list secrets [endpoint](https://developer.hashicorp.com/vault/api-docs/secret/kv/kv-v2#list-secrets)

Each endpoint represents a different way of storing account information in the KV engine of Vault.  The secrets subkeys approach has all accounts stored as key-value pairs in the same secret. The data looks like this:

```text
applications/
              appA/
                    accounts
                      - db_user: pw
                      - app_user: pw
              appB/
                    accounts
                      -db_user: pw
                      -tomcat_user: pw
              ...
```

The list secrets approach has each account stored as its own secret under the application.  The secret contains the password and the secret name itself is the username.

```text
applications/
              appD/
                    db_user 
                      - password: pw
                    app_user 
                      - password:  pw
              appE/
                    db_user 
                      - password: pw
                    tomcat_user 
                      - password:  pw
              ...
```

## Usage

To use the application, do the following:

* [Download](https://releases.hashicorp.com/vault/) Vault OSS.  Mimimum version 1.10.
* Start Vault locally using root as the token name.  A big part of the concept is that the user does not need root creds for the endpoint but policy is not fine tuned. Really just looking at the endpoint.  Anyway, start Vault: `vault server -dev -dev-root-token-id root`
* In another terminal window, set up a python 3.10 environment using [pipenv](https://pipenv.pypa.io/en/latest/)
* Pull this project into your Python environment.
* Run setup/setup.sh script.  This will set environmental variables that the program needs.  So if you skip this part, add the env vars manually.
* The program takes one switch, --mode, which tells it what endpoint to use.  It takes "first" or "second"  If you ran setup, both will work: `python main.py --mode first`
* The script will run and leave a JSON file with the results in the run directory

## Final Words

This is not polished.  I wrote it in a couple of hours.  Don't use it in production.