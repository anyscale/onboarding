# onboarding

Repo to verify an Anyscale onboarding

Steps (for mac)

* `pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/master/35b45a03cffbedcf5720157060276c9c41bb87c0/ray-2.0.0.dev0-cp37-cp37m-macosx_10_13_intel.whl` to ensure you have a pinned nightly

* `pip install -U anyscale` to ensure you have the latest anyscale release

* `anyscale init` to turn this directory into an Anyscale project

* `python driver.py` To create a session and run some code on Anyscale


