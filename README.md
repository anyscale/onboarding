# onboarding

Repo to verify an Anyscale onboarding

Steps (for mac)

* `conda create -n onboarding python=3.7 pip`
* `conda activate onboarding`
* `pip install https://s3-us-west-2.amazonaws.com/ray-wheels/master/b63e493c0414c6e39fefd378d74825fdda2d98d6/ray-2.0.0.dev0-cp37-cp37m-macosx_10_13_intel.whl` to ensure you have a pinned nightly
* `pip install anyscale` to ensure you have the latest anyscale release
* `anyscale cloud setup` to provision anyscale's access to your cloud provider.
  * Provider (aws, gcp): aws
  * Name: Pick any short name, like "mycloud"
* `anyscale init` to turn this directory into an Anyscale project
* `python driver.py` To create a session and run some code on Anyscale

Updated April 28 2021 for anyscale 0.3.55
