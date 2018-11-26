FROM jupyter/datascience-notebook:8ccdfc1da8d5

# launchbot-specific labels
LABEL name.launchbot.io="Programming with Data"
LABEL workdir.launchbot.io="/home/jovyan"
LABEL description.launchbot.io="Programming with Data"
LABEL 8888.port.launchbot.io="Start Tutorial"

# Set the working directory
WORKDIR /home/jovyan

# Modules
# COPY requirements.txt /home/jovyan/requirements.txt
# RUN pip install -r /home/jovyan/requirements.txt

# Add files
COPY notebooks /home/jovyan/notebooks
COPY data /home/jovyan/data

# Allow user to write to directory
USER root
RUN chown -R $NB_USER /home/jovyan \
    && chmod -R 774 /home/jovyan
USER $NB_USER

# Expose the notebook port
EXPOSE 8888

# Start the notebook server
CMD jupyter notebook --no-browser --port 8888 --ip=* --NotebookApp.token='' --NotebookApp.disable_check_xsrf=True 

