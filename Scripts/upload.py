#!/usr/bin/env python
"""
This script uploads raw data to figshare. It should be run on Windows with
a `.figsharerc` file in the user's home directory.
"""
from __future__ import division, print_function
import requests
from requests_oauthlib import OAuth1
import os
import json

article = "XXXXXXX" # TODO


def load_credentials():
    with open(os.path.join(os.path.expanduser("~"), ".figsharerc")) as f:
        cred = json.load(f)
    return cred


def authenticate():
    cred = load_credentials()
    client_key = cred["client_key"]
    client_secret = cred["client_secret"]
    token_key = cred["token_key"]
    token_secret = cred["token_secret"]
    oauth = OAuth1(client_key=client_key, client_secret=client_secret,
            resource_owner_key=token_key, resource_owner_secret=token_secret,
            signature_type='auth_header')
    return oauth


def get_article_details():
    client = requests.session()
    url = "http://api.figshare.com/v1/my_data/articles/{}".format(article)
    oauth = authenticate()
    response = client.get(url, auth=oauth)
    return json.loads(response.content.decode())


def get_uploaded_files():
    return get_article_details()["items"][0]["files"]


def get_uploaded_filenames():
    flist = get_uploaded_files()
    return [f["name"] for f in flist]


def make_local_file_list():
    file_list = []
    raw_dir = os.path.join("Data", "Raw")
    sections = os.listdir(raw_dir)
    for section in sections:
        section_dir = os.path.join(raw_dir, section)
        runs = os.listdir(section_dir)
        for run in runs:
            run_dir = os.path.join(section_dir, run)
            files = os.listdir(run_dir)
            for f in files:
                fpath = os.path.join(run_dir, f)
                file_list.append(fpath)
    return file_list


def make_remote_name(local_path):
    return "_".join(local_path.split("\\")[-3:])


def make_remote_names_dict(local_files=[]):
    remote_names = {}
    if not local_files:
        local_files = make_local_file_list()
    for local_path in local_files:
        fname = "_".join(local_path.split("\\")[-3:])
        remote_names[local_path] = fname
    return remote_names


def get_remote_urls(write=True):
    files = get_uploaded_files()
    remote_urls = {f["name"] : f["download_url"] for f in files}
    if write:
        with open("Config/raw_data_urls.json", "w") as f:
            json.dump(remote_urls, f, indent=4)
    return remote_urls


def upload_file(local_path, remote_name, client=None, oauth=None, verbose=True):
    if not client:
        client = requests.session()
    if not oauth:
        oauth = authenticate()
    files = {"filedata" : (remote_name, open(local_path, "rb"))}
    url = "http://api.figshare.com/v1/my_data/articles/{}/files".format(article)
    response = client.put(url, auth=oauth, files=files)
    results = json.loads(response.content.decode())
    if verbose:
        print("Upload successful")
        for k, v in results.items():
            print(k, ":", v)


def upload_all(overwrite=False):
    local_files = make_local_file_list()
    remote_files = get_uploaded_filenames()
    client = requests.session()
    oauth = authenticate()
    for n, local_path in enumerate(local_files):
        remote_name = make_remote_name(local_path)
        if not remote_name in remote_files or overwrite:
            print("[{}/{}] Uploading {}".format(n+1, len(local_files), local_path))
            upload_file(local_path, remote_name, client=client, oauth=oauth)
        else:
            print("{} already uploaded".format(local_path))
    print("All files uploaded")


def test_upload_file(n=1):
    local_path = make_local_file_list()[n]
    remote_name = make_remote_name(local_path)
    upload_file(local_path, remote_name)


def test_remote_names():
    with open("Config/remote_filenames.json", "w") as f:
        json.dump(make_remote_names_dict(), f, indent=4)


if __name__ == "__main__":
    if os.getcwd()[-7:] == "Scripts":
        print("Changing working directory to experiment root directory")
        os.chdir("../")

    upload_all()
    get_remote_urls()
