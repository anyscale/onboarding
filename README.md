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

* `pip install anyscale` to install anyscale (0.4.3)
* `pip install "ray[default]"` to install ray (1.4.0)

### Cloud Setup

This is a one-time command for your *organization*.  If your administrator has run this command, you don't need to.

`anyscale cloud setup`

You'll be prompted to enter:

  * Provider (aws, gcp): aws
  * Name: Pick any short name, like "mycloud"

### Project initialization

This command creates a project on Anyscale and ties it to this directory.

* `anyscale init` to turn this directory into an Anyscale project

### Run the program

This section creates your anyscale compute cluster and then runs some code on it.
The code that is actually run on Anyscale is contained in the `compute.py` source code file.

* `python driver.py` 

If you run the same command again, the cluster will stil be available and you will not
see significant startup time.
 
* `python driver.py` 

Thank you for onboarding and trying out our product.  We know what you'll appreciate its simplicity
and raw power.




Anyscale 0.4.3
