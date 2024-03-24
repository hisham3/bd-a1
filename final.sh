#!/bin/bash

# get container name or ID
read -p "Container ID or Name: " CONTAINER_NAME

echo "Your ContainerID is $CONTAINER_NAME ."

# Define the full path to the directory inside the container
CONTAINER_DIR='/home/doc-bd-a1'

# Define the full path to the local directory where files should be copied
LOCAL_DIR='service-result'

# Check if the folder exists
if [ ! -d $LOCAL_DIR/ ]; then
  # Folder does not exist, so create it
  mkdir -p $LOCAL_DIR/
  echo "Directory $LOCAL_DIR created."
else
  # Folder exists
  echo "Directory $LOCAL_DIR already exists."
fi

# Copy the output files from the container to the local machine
docker cp $CONTAINER_NAME:$CONTAINER_DIR/res_dpre.csv $LOCAL_DIR/
docker cp $CONTAINER_NAME:$CONTAINER_DIR/eda-in-1.txt $LOCAL_DIR/
docker cp $CONTAINER_NAME:$CONTAINER_DIR/eda-in-2.txt $LOCAL_DIR/
docker cp $CONTAINER_NAME:$CONTAINER_DIR/eda-in-3.txt $LOCAL_DIR/
docker cp $CONTAINER_NAME:$CONTAINER_DIR/vis.png $LOCAL_DIR/
docker cp $CONTAINER_NAME:$CONTAINER_DIR/k.txt $LOCAL_DIR/

# Stop the container
docker stop $CONTAINER_NAME

# Give a message
echo "Files copied and container closed."
