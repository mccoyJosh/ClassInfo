# FROM describes the initial image we are builind our container on. Here we use the official python image!
FROM python:3

# WORKDIR is where our code is going to placed and where the executions are going to run from
WORKDIR /app

# COPY takes two arguements: first one is the file we want to put in the container, and second one is where to put it
COPY requirements.txt ./

# RUN will run a command; we want to do this in the dockerfile to set up the container with all the packages we need
# In our instance, we already have python from the image itself, so all we need is Flask (which is defined
# in the requirements.txt file)
RUN pip install --no-cache-dir -r requirements.txt

# This final command copies EVERYTHING from this directory to the container
# If we want some files to be ignored, we could use a .dockerignore file which works similar to .gitignore files
COPY . .

# This sets up an environment variable
# Here it is commented out because we are not using it, but, it is important to know!
#ENV PORT=8080


# Let's docker know these is a process needing to expose this port
EXPOSE 8080

# This final CMD command is what runs whenever the container is run. YOU CAN ONLY HAVE ONE OF THESE CMD COMMANDS!
CMD [ "python", "./basic_flask.py" ]
