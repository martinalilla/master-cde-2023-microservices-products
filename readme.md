# GCP Microservice Template


---
### To Start
- If you are working in VisualStudio Code, create a launch.json file with the following content:
```
    {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/run.py",
            "env": {
                // adjust pythonpath for local module 
                "PYTHONPATH": "${workspaceFolder}/app"
            },
            "console": "integratedTerminal",
            "justMyCode": false
        }
    ]
}
```
- Create your Virtual Environment: 
    1. Setup a virtual environment
    Set up a virtual environment (optional but recommended), named venv to isolate your project dependencies.
    ```
    python -m venv --copies venv
    ```

    2. Activate the virtual environment
    ```
    .venv\Scripts\activate.bat
    ```
- Install the requirements contained into requirements.txt file
    ```
    pip install -r requirements.txt
    ```
- Start "run.py" using the specific .env file in order to use custom environment variable.
  - With your browser, go to _localhost:8080/docs_


---
### Structure:
- **config**: used for your configurations like:
  - environment variable read
  - secrets data read
  - ecc

- **controller**: Controller pillar of MVC. Here there is all the business logics and it is divided into 2 sub folders:
  - **private**: contains the business logics that should be related to private/internal endpoint calls inside your own backend services
  - **public**: contains the business logics that should be related to your public endpoints

- **model**: Model pillar of MVC. Contains all models, DAO, DTO ecc. There are 2 sub folders:
  - **daos**: contains DBs logics and database data manipulation.
  - **schemas**: data representation useful for business logics, input/output models.
  - **db_schemas**: database data representation.

- **router**: View pillar or MVC. Contains all endpoint divided by functionalities. There are 2 sub folders:
  - **private**: used for private/internal endpoints
  - **public**: used for public endpoints

- **utils**: contains logics that could be re-used. This folder could be (or better, must be) replaces by a private library (PyPi Server or, in GCP, Artifact Registry) in order to share the code among micro-services.

The **v1** folder is used in order to version your code. In this way you can deploy a new version (v2) and at the same time maintain also the older one.
The v1 folder (v2, v3 ecc) is a sub-folder of **app**. This last folder, **app** should be the unique folder you have to deploy. It contains your application code.

---
### public VS private
A public endpoint call is a made by the frontend, for example. It is an external call for which we could be interested to the caller context (who is he):
- we should retrieve caller information from Header A
- we should parse data in way A
- we should take attention to something
- ecc

A private endpoint call is a call made by other internal services (in a micro-services architecture for example):
- we should retrieve caller (the service) information from Header B for audit purposes
- we should parse data in way B (data are safer because we are in an internal call)
- we should take attention to something else
- ecc

A public endpoint must have an authorizations step (RBAC for example. The role should be retrieved from the caller context)

A private endpoint its private. I should decide if check authorization or not.

In this way there are two parallel flows:
- public_router -> public_service -> base_service(some common logics in order to do not duplicate code)
- private_router -> private_service -> base_service(some common logics in order to do not duplicate code)

---

---
### Database 
There is a custom class that mock a DB library.
The DAOs are responsible for the DB management. 
DAOs are not DBs. DAOs **uses** the DBs. The idea is that if you change DB, you have to do some adjustment only into your DAOs. 
Controllers and routers should not be changed.

To use Firestore Emulator:
  ```
    gcloud emulators firestore start --host-port=localhost:8000
  ```

In another terminal, run a firestore.py file to populate data / print results:
  ```
    python firestore.py
  ```
---

### PubSub
To use the PubSub Emulator:
  ```
    gcloud beta emulators pubsub start --project="emedi-dp-dev-prj-assets" --host-port="localhost:8085"
  ```

--- 
### Docker
1. **Build the Docker Image**
    ```
    docker build --build-arg PROJECT_ID=messages -t messagesimage .
    ```

2. **Start the Docker Container**
    ```
    docker run --env-file=.env.development -d --name messagescontainer -p 8080:8080 messagesimage
    ```

### Generate OpenAPI spec
    ```
    set ENVIRONMENT=local
    set PYTHONPATH=./app
    python extract_openapi.py

    ```

### CI/CD
To deploy a stable image in test or production environments, follow these steps:
1. In GCP Console, tag the image in Artifact Registry with the name of the env followed by Semantic Versioning convention.
Example:
    ```
    test-1.0.0
    ```
2. In the environment branch (test or production), add the same tag with git followed by the name of the branch where you want to apply the tag
Example:
    ```
    git rebase -i origin/development
    git tag test-1.0.0 test
    git push origin test-1.0.0
    ```
3. A new build trigger should start with deploy for **test** or **production** environments
