# onboarding

Repo to verify an Anyscale onboarding

Steps (for mac)

* `conda create -n onboarding python=3.7 pip`
* `conda activate onboarding`
* `pip install anyscale` to install anyscale (0.3.56)
* To ensure you have a pinned nightly, `pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/master/1d834bcbe33c7714913fa06c7a7392c29eb7d71d/ray-2.0.0.dev0-cp37-cp37m-macosx_10_13_intel.whl`
* NOTE: If your administrator has run this command, you don't need to:
  `anyscale cloud setup` to provision anyscale's access to your cloud provider.
  * Provider (aws, gcp): aws
  * Name: Pick any short name, like "mycloud"
* `anyscale init` to turn this directory into an Anyscale project
* `python driver.py` To create a session and run some code on Anyscale

Anyscale 0.3.56
