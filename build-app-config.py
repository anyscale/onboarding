# if you want to you can craete the onboarding app config by running this script
import os
import time
import anyscale
import yaml
import json
from anyscale.sdk.anyscale_client.sdk import AnyscaleSDK

def read_token():
    creds_file = os.path.expanduser("~/.anyscale/credentials.json")
    token = json.load(open(creds_file,))["cli_token"]
    return token

def project_id():
    project_yaml = yaml.full_load(open(".anyscale.yaml"))
    return project_yaml["project_id"]

TOKEN = read_token()
project_id = project_id()
sdk = AnyscaleSDK(TOKEN)

def bootstrap_app_config():
    starter_app_config = sdk.create_app_config(
            {"project_id":project_id, 
                "name":"onboard", 
                "config_json": 
                {
                    "base_image":"anyscale/ray-ml:pinned-nightly",
                    "post_build_cmds":["echo 'Hello from onboarding.' > build.log"]
                }
            })
    return starter_app_config.result.id

bootstrap_app_config()
