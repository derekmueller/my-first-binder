# my-first-binder
 A binder tutorial
 
# Sharing Jupyter Notebooks with Binder

Binder is a Project Jupyter effort to create a means of sharing computing environments. The main tools in the Binder project are repo2docker and BinderHub. repo2docker converts code repositories into reproducible Docker images. BinderHub is a web application that allows users to create sharable, interactive, reproducible environments from code repositories. It uses repo2docker to generate Docker images for each environment, and JupyterHub to provide interactive user sessions from those images.

mybinder.org is a community run deployment of BinderHub that allows users to share Python scripts and Jupyter Notebooks along with the necessary dependencies. All that is needed is a public GitHub repo with one or more scripts and/or notebooks, an environment definition file, and a related mybinder.org URL. Once shared, other users can run your files in an interactive JupyterLab session using the iPython notebook editor or console, or a virtual terminal. An edits made to the files are not persistent so there is no need to worry about the source repo being changed. If your scripts or notebooks require input data then just put those files in the repo as well, provided they are not too big (ideally less than 10 MB).

The following is a simplified guide to using mybinder.org and is based off the tutorial found [here](https://the-turing-way.netlify.app/communication/binder/zero-to-binder.html).

## Step 1 - Create the Repo and Files

1. Create a public repo on GitHub. Let's call it `my-first-binder`
2. Create the environment definition file. This can use [pip's `requirements.txt` format](https://pip.pypa.io/en/stable/reference/requirements-file-format/), or the Conda [`environment.yml` format](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually). Let's use the `environment.yml` format since so much of what we are doing involves Conda. For this example, create a file called `environment.yml`, put the following lines in it, and then commit it to the `main` branch of the repo.

``` yml
name: geo_env
channels:
  - conda-forge
dependencies:
  - python
  - geopandas
```

3. Create a Python script called `geo_script.py`, add the following lines, and commit it to the `main` branch of the repo.

``` python
import geopandas as gpd

# Import sample data
gdf = gpd.read_file("ne_110m_admin_0_countries.gpkg")

# Print column names
print(gdf.columns)
```

4. Create a Jupyter notebook called `geo_notebook.ipynb`, add the following lines to the first cell, and commit it to the `main` branch of the repo.

``` python
import geopandas as gpd

# Import sample data
gdf = gpd.read_file("ne_110m_admin_0_countries.gpkg")

# Display first 5 rows
display(gdf.head())
```

5. Add the sample dataset to the repo. Copy `ne_110m_admin_0_countries.gpkg`  into the `main` branch of the repo. If the link is broken just make a GeoPackage from [this shapefile](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip) or modify the code to use a different sample dataset.

## Step 2 - Build the Binder Environment

1. Go to [mybinder.org](https://mybinder.org/)
2. In the `Github repository name of URL` box, enter the URL to your repo. E.g., `https://github.com/{my_user_name}/my-first-binder`
3. Optional: If you want to create a link directly to a notebook then enter it's name in the `Path to a notebook file (optional)` box.
4. Click on the orange `launch` button to build the environment. A status bar should appear below. If the environment has already been built then JupyterLab should launch in a few moments. If then environment has not been built yet then a log should be displayed which shows the progress. It can take a few minutes to built a new environment, especially when relatively large dependencies like GeoPandas are required. Once the environment is built it will be quite quick to launch it again in the future.
5. The JupyterLab interface should launch when it is ready. To open the `geo_notebook.ipynb` notebook click on its name in the File Browser. Running the first cell should display the first 5 rows in the GeoDataFrame.

## Step 3 - Running python scripts in Binder
1. To run the script in the repo click on `Terminal` in the `Launcher` pane and then run the following from the command line: `python geo_script.py`. The column names of sample dataset should be printed.

## Step 4 - Share the Binder Environment

1. Go back to [mybinder.org](https://mybinder.org/)
2. Enter the URL to your repo again.
3. A mybinder.org URL will be generated in the `Copy the URL below and share your Binder with others` box. Something like: [https://mybinder.org/v2/gh/{my_user_name}/my-first-binder/HEAD](https://mybinder.org/v2/gh/{my_user_name}/my-first-binder/HEAD). You can now share this URL with anyone you would like.
4. If you want to include a binder badge in the readme of your repo, just copy the text in the `Expand to see the text below, paste it into your README to show a binder badge` box and paste it into your `readme.md`


Thanks to [John Foster](https://github.com/johnofoster/) for this!  
