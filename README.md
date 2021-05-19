# onboarding

Repo to verify an Anyscale onboarding.  This process changes frequently as our beta product evolves
so check back frequently!

## Steps (for mac)

### Environment.

This section makes sure you have a clean working predictable python environment.  Advanced
users have a way of doing this already, so you may skip it.

* `conda create -n onboarding python=3.7 pip`
* `conda activate onboarding`

### Python clients

This section has the steps to install `anyscale` and `ray`, both of which are distributed as pip packages.

* `pip install anyscale` to install anyscale (0.3.56)
* Install a pinned nightly.  The first link is the one for Mac and Python 3.7.
```
pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/master/1d834bcbe33c7714913fa06c7a7392c29eb7d71d/ray-2.0.0.dev0-cp37-cp37m-macosx_10_13_intel.whl

pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/master/1d834bcbe33c7714913fa06c7a7392c29eb7d71d/ray-2.0.0.dev0-cp38-cp38-macosx_10_13_x86_64.whl

pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/master/1d834bcbe33c7714913fa06c7a7392c29eb7d71d/ray-2.0.0.dev0-cp37-cp37m-manylinux2014_x86_64.whl

pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/master/1d834bcbe33c7714913fa06c7a7392c29eb7d71d/ray-2.0.0.dev0-cp38-cp38-manylinux2014_x86_64.whl
```

### Cloud Setup

This is a one-time command for your *organization*.  If your administrator has run this command, you don't need to.

`anyscale cloud setup`

You'll be prompted to enter:

  * Provider (aws, gcp): aws
  * Name: Pick any short name, like "mycloud"

### Project initialization

This command creates a project on Anyscale and ties it to this directory.

* `anyscale init` to turn this directory into an Anyscale project

### Build Config Creation

Running this script uses the Anyscale SDK to create an App Config on Anyscale.  This App Config
is a definition of an environment on Anyscale in which to run a distributed application.

* `python build_app_config.py`

Note: This command takes several minutes to complete.  Go to the anyscale UI to see your progress.
If you have already run this command, then it will error out because the App Config already exists.

### Run the program

This section creates your anyscale compute cluster and then runs some code on it.
The code that is actually run on Anyscale is contained in the `compute.py` source code file.

* `python driver.py` 

If you run the same command again, the cluster will stil be available and you will not
see significant startup time.
 
* `python driver.py` 

Thank you for onboarding and trying out our product.  We know what you'll appreciate its simplicity
and raw power.




Anyscale 0.3.56
