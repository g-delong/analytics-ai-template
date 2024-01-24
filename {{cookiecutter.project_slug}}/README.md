# {{cookiecutter.project_name}}


Welcome to {{cookiecutter.project_name}}! This project was generated from a template using [cookiecutter](https://www.cookiecutter.io/) designed for the Geisinger AI Lab.


## 👋 Introduction

You can get started in a Sagemaker notebook terminal by running the following commands:

```bash
# Set up a Python virtual environment
conda create -n {{cookiecutter.project_slug}} python=3.9
conda activate {{cookiecutter.project_slug}}
# Install requirements & integrations
make setup
# Connect to zenml server 
zenml init
```

You can now run the pipeline locally: 

```
# Run the pipeline
python run.py
```

Refactor the pipeline and steps, and add logic inside the
`src` directory as needed for your project. 

If a remote zenml server is available, you can connect to the server.

```
zenml connect --url http://ip-address:port --username default --password ""
```

Once connected, you can list available stacks and set the active stack:

```
zenml stack list

zenml stack set {stack_name}
```

For more information on zenml, send a Teams chat message to the GAIL team.
