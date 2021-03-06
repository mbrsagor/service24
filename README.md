# service24 online service provider 

## Setup

### Dependencies

- Python 3.8.5
- Django 3.0.5
- MongoDB 4.0.14

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop 
on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

###### On Mac
First you will install mongo in your system.

````
brew tap mongodb/brew
brew install mongodb-community@4.0
mongod --config /usr/local/etc/mongod.conf --fork
ps aux | grep -v grep | grep mongod
````

Create the database by running the following commands in a mongo shell
```angular2html
mongo
use service24
```

### Setup Django Server (Mac)
We're using python3 instead of python2.x. If you don't have python3 installed,
install [Homebrew](http://brew.sh), then…

```
brew install python3
```

Assuming you've cloned the repository, open Terminal and `cd ~/your/path/to/service24`.


```bash/zsh
virtualenv venv --python=python3.8
```

Activate it:

```bash
source venv/bin/activate
```

###### Config database on the project.
> First go to `config` folder then change the file name db_sample => db_development.py

Install the python dependencies which includes django and other libraries.

```
pip install -r requirements.txt
```

#### Run server locally
```
./manage.py migrate
./manage.py runserver
```
