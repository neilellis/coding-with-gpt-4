
Prompt:

```
Write a single file python app that gets tweets from Twitter API v2.0, uses carmen to infer their location (Carmen 2.0
supports Twitter API 2.0) and then use nuts_finder to add the nuts locations also. Then place the tweets into
appropriate mysql database tables such that all fields in the tweet are stored. The tables should be normalized and have
foreign key relationships. Make sure that the NUTS data should have it's own table.

All credentials are stored in a .env file.

Then supply the requirements.txt to run this.
```

Fixes:

This produced the app.py file and the requirements.txt, but because GPT-4 is out of date it put in the wrong versions of
library files.

E.g.

```
ERROR: Could not find a version that satisfies the requirement carmen==1.1.0 (from versions: 0.0.3, 0.0.4, 2.0.0)
ERROR: No matching distribution found for carmen==1.1.0
```

I fixed up the requirements file, but now I want to Dockerize all of this so I can run it and a mysql database using
docker compose. So next I asked for the Dockerfile and the result needed no corrections. And then I asked for a
docker-compose file, note I didn't mention MySQL. It did not use the .env values, so I changed the file to do that and
removed a port 80 entry too. Finally to make things neater I gave the db container a simple name of ```db```

```Dockerfile
version: '3.9'

services:
  app:
    build: .
    environment:
      - BEARER_TOKEN=${BEARER_TOKEN}
      - MYSQL_HOST=db
      - MYSQL_USER=tweets
      - MYSQL_PASSWORD=tweets
      - MYSQL_DATABASE=tweets
    depends_on:
      - db

  db:
    name: db
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_USER=tweets
      - MYSQL_PASSWORD=tweets
      - MYSQL_DATABASE=tweets
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:

```

### Working through the issues.

Running the docker compose command produced the following error:

```
#0 8.549   
#0 8.549   × python setup.py egg_info did not run successfully.
#0 8.549   │ exit code: 1
#0 8.549   ╰─> [12 lines of output]
#0 8.549       Failed `CDLL(libgeos_c.so.1)`
#0 8.549       Failed `CDLL(libgeos_c.so)`
#0 8.549       Traceback (most recent call last):
#0 8.549         File "<string>", line 2, in <module>
#0 8.549         File "<pip-setuptools-caller>", line 34, in <module>
#0 8.549         File "/tmp/pip-install-vxdniyc5/shapely_b169bd449dac43e38253af94b5360a5d/setup.py", line 80, in <module>
#0 8.549           from shapely._buildcfg import geos_version_string, geos_version, \
#0 8.549         File "/tmp/pip-install-vxdniyc5/shapely_b169bd449dac43e38253af94b5360a5d/shapely/_buildcfg.py", line 166, in <module>
#0 8.549           lgeos = load_dll('geos_c',
#0 8.549         File "/tmp/pip-install-vxdniyc5/shapely_b169bd449dac43e38253af94b5360a5d/shapely/_buildcfg.py", line 159, in load_dll
#0 8.549           raise OSError(
#0 8.549       OSError: Could not find library geos_c or load any of its variants ['libgeos_c.so.1', 'libgeos_c.so']
#0 8.549       [end of output]
#0 8.549 
```

Passing this back to GPT-4 got:

t looks like the Shapely package, which is a dependency of the nuts_finder package, requires the GEOS library, but it's
not available in the Python slim image you're using. To resolve this issue, you can update your Dockerfile to install
the required library before installing the Python packages.

Here's an updated version of your Dockerfile:

```Dockerfile

# Use an official Python runtime as a parent image

FROM python:3.9-slim

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install system dependencies for GEOS library

RUN apt-get update && apt-get install -y \
libgeos-dev \
&& rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container

EXPOSE 80

# Define environment variable

ENV NAME World

# Run app.py when the container launches

CMD ["python", "app.py"]

```

Next I had issues with Carmen and tweepy that made me realise I had not asked ChatGPT to use the **search** API so I decided to

```
Please use the v2 search in tweeps not home_timeline
```
Which correctly updated the app.py

Next

```
#0 2.915 ERROR: Cannot install -r requirements.txt (line 1) and -r requirements.txt (line 4) because these package versions have conflicting dependencies.
#0 2.916
#0 2.916 The conflict is caused by:
#0 2.916     tweepy 4.13.0 depends on requests<3 and >=2.27.0
#0 2.916     nuts-finder 21.5.5.14 depends on requests==2.22.0
#0 2.916
```

This was a unresolvable dependency conflict, so I asked ChatGPT to fix it:

```
tweepy 3.10 does not support twitter api v2.0
```

And I got:


You're correct that Tweepy 3.10.0 does not support Twitter API v2.0. In this case, you have a few options to resolve the dependency conflict between tweepy and nuts-finder:

Fork and modify nuts-finder to use a newer version of requests. You can fork the nuts-finder repository, update its requirements.txt file to use a newer version of requests, and then use your forked version in your project. This way, you can keep using the latest version of Tweepy.
To do this:

Fork the nuts-finder repository: https://github.com/EU-DEX/nuts-finder
Update the requirements.txt file in your fork to use requests>=2.22.0 instead of requests==2.22.0.
In your project's requirements.txt file, replace nuts_finder with the URL of your forked repository, like this:
```
tweepy
carmen
git+https://github.com/your_username/nuts-finder.git
requests>=2.27.0
mysql-connector-python
python-dotenv
```
Replace your_username with your GitHub username.

So I did, the repository URL it gave was incorrect, I found the right one and did as I was told:

Ah-haha

```
> [5/5] RUN pip install --trusted-host pypi.python.org -r requirements.txt:                                                                                                                                                                                                                                       
#0 1.220 Collecting git+https://github.com/neilellis/nuts_finder.git (from -r requirements.txt (line 4))                                                                                                                                                                                                           
#0 1.221   Cloning https://github.com/neilellis/nuts_finder.git to /tmp/pip-req-build-3uj3dgc_                                                                                                                                                                                                                     
#0 1.225   ERROR: Error [Errno 2] No such file or directory: 'git' while executing command git version                                                                                                                                                                                                             
#0 1.225 ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH?
```  

Chat-GPT correctly changed the dockerfile to:

```Dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev default-libmysqlclient-dev libgeos-dev git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .
CMD ["python", "app.py"]
```

Next:

```
6.217       Traceback (most recent call last):
#0 6.217         File "/usr/local/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 363, in <module>
#0 6.217           main()
#0 6.217         File "/usr/local/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 345, in main
#0 6.217           json_out['return_val'] = hook(**hook_input['kwargs'])
#0 6.217         File "/usr/local/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 130, in get_requires_for_build_wheel
#0 6.217           return hook(config_settings)
#0 6.217         File "/tmp/pip-build-env-y0f_3ol0/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 338, in get_requires_for_build_wheel
#0 6.217           return self._get_build_requires(config_settings, requirements=['wheel'])
#0 6.217         File "/tmp/pip-build-env-y0f_3ol0/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 320, in _get_build_requires
#0 6.217           self.run_setup()
#0 6.217         File "/tmp/pip-build-env-y0f_3ol0/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 335, in run_setup
#0 6.217           exec(code, locals())
#0 6.217         File "<string>", line 2, in <module>
#0 6.217       ModuleNotFoundError: No module named 'nuts_finder'
#0 6.217       [end of output]
#0 6.217   
```
ChatGPT is on the case:

Changing the Dockerfile to:

FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev default-libmysqlclient-dev libgeos-dev git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt && \
pip install git+https://github.com/neilellis/nuts_finder.git

COPY . .
CMD ["python", "app.py"]

Then

```bash
8.650           return hook(config_settings)
#0 8.650         File "/tmp/pip-build-env-entgptfi/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 338, in get_requires_for_build_wheel
#0 8.650           return self._get_build_requires(config_settings, requirements=['wheel'])
#0 8.650         File "/tmp/pip-build-env-entgptfi/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 320, in _get_build_requires
#0 8.650           self.run_setup()
#0 8.650         File "/tmp/pip-build-env-entgptfi/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 335, in run_setup
#0 8.650           exec(code, locals())
#0 8.650         File "<string>", line 2, in <module>
#0 8.650       ModuleNotFoundError: No module named 'nuts_finder'
#0 8.650       [end of output]
#0 8.650   
```

CHatGPT:
Apologies for the inconvenience. It seems that the issue still persists. Let's try a different approach by cloning the nuts_finder repository and installing it directly in your project folder.

First, remove the nuts_finder related lines from your Dockerfile. Your updated Dockerfile should look like this:

```dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev default-libmysqlclient-dev libgeos-dev git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .
CMD ["python", "app.py"]
```
Next, clone the nuts_finder repository directly into your project folder:

```bash
git clone https://github.com/neilellis/nuts_finder.git
``
Now, update your app.py to import nuts_finder from the local folder:

```python
Copy code
import sys
sys.path.append('./nuts_finder')
```
Add this snippet at the beginning of your app.py, before the other imports.

Rebuild your Docker containers and run docker-compose up again. The app should now build and work without any issues.


So I did,



```
The `tweet.fields` query parameter value [user] is not one of [attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,edit_history_tweet_ids,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld]
```

So this was fiexed to
```
tweets = client.search_recent_tweets(query, tweet_fields=["id", "text", "author_id", "created_at", "public_metrics", "geo"], max_results=tweet_count).data
```

Note the additional ```.data``` yep GPT missed that one.

Okay so finally I put in my fixed query

```bash
    query = "floods -is:retweet -is:quote -is:reply"  # Replace with your desired search query
```

Okay that's progress but still it's persisting the data incorrectly:

... AND SO ON
