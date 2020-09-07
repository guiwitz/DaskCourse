# Remote connection to Jupyter and Dask on a cluster

## Install conda and create an dask environment

1. Install miniconda. For example:

    ```
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

2. create an environment with jupyter and dask (use e.g. the course environment.yml file):

    ```
    git clone https://github.com/guiwitz/DaskCourse.git
    cd DaskCourse/binder
    conda env create -f environment.yml
    ```

## Run dask in Jupyter
As one should not run computations directly on the login node of the cluster, one has to run an interactive job to run Jupyter.

1. Allocate resources for interactive job, e.g.:

    ```
    salloc --mem 16GB --time 1:00:00 --cpus-per-task=4 --ntasks=1
    ```

2. Once your job is running, the commmand will return a jobid number. Use that number to enter the interactive job (of course replace the number with yours). Note that you will also see information regarding on which node your job is running, e.g. anode2020:

    ```
    srun --jobid=33896954 --pty bash
    ```

3. Now you can start Jupyter. Firs take care of a configuration issue (see https://stackoverflow.com/questions/35878178/jupyter-notebook-permission-error):

    ```
    export XDG_RUNTIME_DIR=""
    ```

4. Activate your environment

    ```
    source activate dask_course
    ```
 
5. Start Jupyter and specify a specific port

    ```
    jupyter-lab --no-browser --port=8889 --ip=0.0.0.0
    ```

## Accessing the remote Jupyter in your browser

1. There is no way to "forward" Jupyter directly to your computer (as with X-forwarding applications). You therefore need to create an ssh tunnel between the cluster port and a port on your computer. To do that first, open a NEW terminal. The syntax for the tunnel is ```your_local_port:node_name:cluster_jupyter_port```. For example here where we are running on the node anode220 and have started Jupyter on port 8889, we can use:

    ```
    ssh -N -f -L 8889:anode220:8889 your_user_name@submit.unibe.ch
    ```

2. Now in your local browser you can simply go to http://localhost:8889 and you will have access to Jupyter (use the token that appeared at startup of Jupyter)

3. The dashboard of Dask starts on port 8787. To also have access to it on your local machine, just follow the same procedure as above to open a tunnel on port 8787. Open a new terminal and use:

    ```
    ssh -N -f -L 8787:anode220:8787 your_user_name@submit.unibe.ch
    ```

4. Now you can go to http://localhost:8787 to see the dashboard

5. When you scale your dask cluster, you can monitor jobs using the classic command in a new terminal.

    ```
    squeue -u your_user_name
    ```
