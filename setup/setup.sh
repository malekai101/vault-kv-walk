#!/usr/bin/env bash

# shellcheck disable=SC1068
export VAULT_ADDR="http://localhost:8200"
export VAULT_TOKEN="root"

# first way
vault kv put secret/first_way/applications/appA/accounts db_user=foo app_user=bar web_user=baz >/dev/null 2>&1
vault kv put secret/first_way/applications/appB/accounts db_user=tim tomcat_user=password >/dev/null 2>&1
vault kv put secret/first_way/applications/appC/accounts admin=supersecure >/dev/null 2>&1

#second way
vault kv put secret/second_way/applications/appD/db_user password=fruit >/dev/null 2>&1
vault kv put secret/second_way/applications/appD/app_user password=tree >/dev/null 2>&1
vault kv put secret/second_way/applications/appD/web_user password=basket >/dev/null 2>&1
vault kv put secret/second_way/applications/appE/admin_user password=box >/dev/null 2>&1
vault kv put secret/second_way/applications/appE/random_user password=game >/dev/null 2>&1
vault kv put secret/second_way/applications/appF/all_user password=printer >/dev/null 2>&1


