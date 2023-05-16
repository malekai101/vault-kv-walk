# This is a sample Python script.
import pprint

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import argparse
import os
import json
from datetime import datetime

parser = argparse.ArgumentParser(description='Process input.')
parser.add_argument('--mode', default="second")

def get_vault_variables():
    vault_info = {"addr": os.getenv("VAULT_ADDR"), "token": os.getenv("VAULT_TOKEN")}
    return vault_info


def add_app_to_data(data, app):
    data[app] = []
    return data


def add_user_to_app(data, app, user):
    list.append(data[app], user)
    return data


def write_doc(data, mode):
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{mode}.json"
    json_obj = json.dumps(data)
    with open(filename, "w") as filehandle:
        filehandle.write(json_obj)
    print(f"Wrote doc {filename}")

def base_vault_rest(basepath, token, childpath, verb):
    url = f"{basepath}/v1/{childpath}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Vault-Token": token,
    }
    try:
        resp = requests.request(method=verb, url=url, headers=headers)
        resp.raise_for_status()
        payload = resp.json()
        if "data" in payload:
            return payload["data"]
        else:
            raise Exception("data section missing from credentials return.")
    except Exception as exp:
        print(f"Failed to get database login info from vault: {exp}")
        raise

def list_vault(basepath, token, childpath):
    return base_vault_rest(basepath, token, childpath, "LIST")


def get_vault(basepath, token, childpath):
    return base_vault_rest(basepath, token, childpath, "GET")


def second_way():
    print("Operating in second mode")
    vault_info = get_vault_variables()
    #Get the apps
    apps = list_vault(vault_info["addr"], vault_info["token"],
                          "secret/metadata/second_way/applications/")["keys"]
    data = {}
    for app in apps:
        app_clean = app[:-1]
        print(f"Application: {app_clean}")
        add_app_to_data(data, app_clean)
        users = list_vault(vault_info["addr"], vault_info["token"],
                               f"secret/metadata/second_way/applications/{app_clean}")["keys"]
        for user in users:
            print(f"\tUser: {user}")
            add_user_to_app(data, app_clean, user)
    write_doc(data, "second")
    return

def first_way():
    print("Operating in first mode")
    vault_info = get_vault_variables()
    # Get the apps
    apps = list_vault(vault_info["addr"], vault_info["token"],
                          "secret/metadata/first_way/applications/")["keys"]
    data = {}
    for app in apps:
        app_clean = app[:-1]
        print(f"Application: {app_clean}")
        add_app_to_data(data, app_clean)
        users = get_vault(vault_info["addr"], vault_info["token"],
                               f"secret/subkeys/first_way/applications/{app_clean}/accounts")["subkeys"]
        for user in users:
            print(f"\tUser: {user}")
            add_user_to_app(data, app_clean, user)
    write_doc(data, "first")
    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    args = parser.parse_args()
    if args.mode == "first":
        first_way()
    elif args.mode == "second":
        second_way()
    else:
        print(f"{args.mode} is bad input")

