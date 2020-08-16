# service24 

## Setup

### Dependencies

- Python 3.8.5
- Django 3.0.5
- MongoDB 4.0.14

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps.If you've developed django apps on Windows, you should have little problem getting up and running.

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

Install the python dependencies which includes django and other libraries.

```
pip install -r requirements.txt
```

#### Run server locally
```
./manage.py migrate
./manage.py runserver
```

## Developer Guidelines
1. You have to follow [PEP8](https://www.python.org/dev/peps/pep-0008/).
2. Yoh have to merge first forward only. See [how](http://ariya.ofilabs.com/2013/09/fast-forward-git-merge.html).
3. After merging the Pull Request, delete the branch from remote. Only specific branch `master` should be in remote.

   `git push origin --delete <branchName>`
