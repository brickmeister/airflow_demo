
# Databricks Airflow Demo

This is a demonstration of Databricks Airflow integration to utilize directed acyclic graphs (DAGs) to orchestrate adn schedule jobs.

# Table of Contents
- [Databricks Airflow Demo](#databricks-airflow-demo)
- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Installing Airflow Databricks integration](#installing-airflow-databricks-integration)
  - [Obtaining a Databricks token](#obtaining-a-databricks-token)
  - [Setting up airflow](#setting-up-airflow)
    - [Initialize the database](#initialize-the-database)
    - [Setup an airflow user](#setup-an-airflow-user)
  - [Running the Airflow server](#running-the-airflow-server)
  - [Run the Airflow scheduler](#run-the-airflow-scheduler)
- [Access the Airflow UI](#access-the-airflow-ui)

# Requirements
* Databricks Account
* Airflow Server
* Access to Cloud Storage or DBFS

# Setup

## Installing Airflow Databricks integration
Run the following command to install airflow with databricks integration. See [databricks airflow integration](https://docs.databricks.com/dev-tools/data-pipelines.html#install-the-airflow-databricks-integration) for more details.
```{sh}
$ pip3 install "apache-airflow[databricks]" "apache-airflow[cncf.kubernetes]"
```

## Obtaining a Databricks token
The databricks personal access token can be obtained from the Databricks workspace. Please follow instructions detailed in [getting a databricks access token](https://docs.databricks.com/sql/user/security/personal-access-tokens.html).

## Setting up airflow
For the purpose of this workshop, we'll use a local instance of airflow.

### Initialize the database
Run the following command to initialize the airflow database. See [airflow startup](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html) for more info.

```{sh}
$ export AIRFLOW_HOME=${PWD}/airflow
$ airflow db init
```

### Setup an airflow user
Run the following command to setup an airflow user.
```{sh}
$ export AIRFLOW_HOME=${PWD}/airflow
$ airflow users create \
            --username admin \
            --firstname Peter \
            --lastname Parker \
            --role Admin \
            --email spiderman@superhero.org
```

## Running the Airflow server
Run the following command below to run the airflow server
```{sh}
$ export AIRFLOW_HOME=${PWD}/airflow
$ airflow webserver --port 8080 -D
```

## Run the Airflow scheduler
Run the follow command to run the airflow scheduler.
```{sh}
$ export AIRFLOW_HOME=${PWD}/airflow
$ airflow scheduler
```

# Access the Airflow UI
Login the airflow UI with the credentials specified above in [setting up airflow user](###setup-an-airflow-user) at [http://localhost:8080](http://localhost:8080)