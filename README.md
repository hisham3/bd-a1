
##### Nile University | Spring 2024 | CSCI461 Introduction to Big Data

# Big Data Analytics Assignment: Containerized Data Processing Pipeline

This assignment involves setting up a local directory, creating a Docker container with specific configurations, and implementing a data processing pipeline using Python. The pipeline will include data loading, preprocessing, exploratory data analysis, visualization, and implementing a K-means clustering model. Finally, a bash script will manage the output files and container lifecycle.



## Packages and Libraries

- sys
- subprocess
- sklearn
- pandas
- matplotlib
- seaborn
## Setup Local Environment

- **Create Local Directory**:
    Establish a directory on your local machine named `bd-a1/`.

- **Download Dataset**:
    Obtain a simple dataset from the [Kaggle](https://www.kaggle.com/datasets/lewisduncan93/the-economic-freedom-index) and place it in the `bd-a1/` directory.


## Dockerfile Configuration

- **Base Image Specification**:
    Use `Ubuntu` as the base image for the Docker container.
        
        FROM ubuntu

- **Package Installation**:
    Install essential packages within the Dockerfile: Python3, Pandas, Numpy, Seaborn, Matplotlib, scikit-learn, and Scipy.
        
        # Update the package list
        RUN apt update -y

        # Upgrade any existing packages
        RUN apt upgrade -y

        # Install Python 3 and pip, the Python package installer
        RUN apt install python3 -y
        RUN apt install python3-pip -
        
        # Install Python packages using pip
        RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy openpyxl


- **Directory Creation in Container**:
    Create a directory at /home/doc-bd-a1/ inside the container.

        # Set the working directory in the container to /home/doc-bd-a1/
        WORKDIR /home/doc-bd-a1/

- **Dataset File Transfer**:
    Copy the dataset file into the container.

        # Copy the economic data Excel file into the container
        COPY ./economic_freedom_index2019_data.xlsx ./

- **Container Startup Behavior**:
    Configure the container to open a bash shell upon startup.

    You need first to build the Dockerfile then run the image
        
        docker build -t bd-a1 <Dockerfile-Path>
        docker run -it bd-a1 bash







## Python File Creation and Execution

- **File Creation**: After running the container with bash, the following command will create the required files.
    
        touch load.py dpre.py eda.py vis.py model.py

    
    Then, you have to use `nano` command for each files to write the python code.

    **final.sh**:
        create a bash script `locally` to copy output files from the container to bd-a1/service-result/ and stop the container.

        docker cp $CONTAINER_NAME:$CONTAINER_DIR/<FILENAME> $LOCAL_DIR/


- **Execution**: After creating file you need to initialize the pipline by running `load.py` file with the dataset path as an argument.

        python3 load.py ./economic_freedom_index2019_data.xlsx



## Bonus Tasks
- **Docker Hub** :
    Push the Docker image to Docker Hub.

    [![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/repository/docker/hesmamdouh/bd-a1/general)

        docker tag bd-a1 <username>/bd-a1

        docker login -u <username>

        docker push <username>/bd-a1

- **GitHub Repo**:
    Push all your files to a GitHub repository.
    
    [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hisham3/bd-a1)

        git init
        git add .
        git commit -m "message"
        git branch -M main
        git remote add origin https://github.com/hisham3/hisham3.git
        git push -u origin main

## Authors

- Hesham Mamdouh
- Adel Saeed
- Abdulrahman Radwan
- Mohamed Abdulaziz


