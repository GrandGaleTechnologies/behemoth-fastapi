# 🚀 Behemoth FastAPI

A powerful, scalable template to kickstart your backend projects. Includes FastAPI with Docker integration and JWT authentication for quick development of robust and secure APIs.Inspired by [Radoslav Georgiev's Django Structure for Scale lecture](https://youtu.be/yG3ZdxBb1oo?si=D6A9dHyhKb_Kf-J7) and my own personal experience, this template offers a structured approach to building scalable web applications.


## 📑 Table of Contents
- [🚀 Behemoth FastAPI](#-behemoth-fastapi)
  - [📑 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [📁 Project Structure](#-project-structure)
  - [Getting Started](#getting-started)
  - [Deploy](#deploy)
  - [🤝 Contribute to the Project](#-contribute-to-the-project)
  - [📬 Contact](#-contact)


## ✨ Features

**.vscode:** Configuration files for Visual Studio Code.

**alembic/:** Contains Alembic settings and migrations.

**app/:** The main FastAPI project directory.
  - **author/**: Example structure for modular design, allowing easy decoupling
    - **schemas/:** Contains structured schemas used across the app.
    - **apis.py:**  Stores all API route definitions.
    - **crud.py:** Contains CRUD operations.
    - **exceptions.py:** Stores custom exceptions.
    - **formatters.py:** Holds formatting functions.
    - **models.py:** Defines database models
    - **selectors.py:** Handles data retrieval operations..
    - **services.py:** Manages data modification operations (POST, PUT, DELETE).
    - 
  - **common/**: Contains shared utilities and general functionalities. 
    - **annotations.py:**  Stores custom type annotations.
    - **auth.py:** Manages authentication.
    - **crud.py:** Where all the general/generic CRUD classes will be kept.
    - **dependencies.py:** Defines dependencies used across modules.
    - **exceptions.py:** Where all the general/generic exceptions are kept.
    - **paginators.py:** Collection of helpers for response pagination.
    - **schemas.py:** Where you will keep your general/generic schemas.
    - **security.py:** Where all the security functions are kept.
    - **types.py:** Contains common types used in the application.
    - **utils.py:** General utility functions.
  - **Core/**: Core functionalities of the application.
    - **database.py:** Database connection and session management.
    - **handlers.py:** Exception handlers.
    - **settings.py:** Environment configuration settings.
    - **tags.py:** Route tags.
  - **external/**: Entry point and external dependencies.
    - **main.py:**: Main application entry point.
**tests.py/** Houses all application tests.
**env_sample.txt:** Sample environment variables.
**.flake8:** Contains the configurations for flake8
**.gitignore:** Specifies which folders/files to not push to github
**.pylintrc:** Contains the configurations for pylint
**alembic.ini:** Contains all the configurations for alembic
**docker-compose.yml:** Docker configurations for containerized setup.
**Dockerfile:** Instructions to build docker image.
**LICENSE:** This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
**pytest.ini:** Where all the pytest configurations will be kept
**railway.toml:** Contains all the railway configurations
**requirements.txt:** Lists all application dependencies.
**start.sh:** Application start up processes


## 📁 Project Structure

```plaintext
.vscode
alembic/
app/
    author/
        schemas/
          __init__.py
          base.py
          create.py
          edit.py
          response.py
        __init__.py
        apis.py
        crud.py
        exceptions.py
        formatters.py
        models.py
        selectors.py
        services.py
    common/
        __init__.py
        annotations.py
        auth.py
        crud.py
        dependencies.py
        exceptions.py
        paginators.py
        schemas.py
        security.py
        types.py
        utils.py
    core/
        __init__.py
        database.py
        handlers.py
        settings.py
        tags.py
    external/
        __init__.py
        main.py
  tests/
    __init__.py
.env_sample
.flake8
.gitignore
.pylintrc
alembic.ini
docker-compose.yml
Dockerfile
LICENSE
pytest.ini
raiway.toml
README.md
requirements.txt
start.sh
```


## Getting Started

1. Setup Virtual Environment (If you are not using docker)
   ```shell
  $python -m venv .venv
  $.venv\Scripts\activate  # Windows
  $source .venv/bin/activate  # macOS/Linux
   ```
   NOTE: If you are using you can use create environment and it will be created and selected as workspace

</br>
1. Install dependencies:
   Locally

   ```shell
   $ pip install -r requirements.txt
   ```
</br>
    With Docker
   
   ```shell
   docker-compose up
   ```
</br>

1. Create a `.env` file and input environment variables.
</br>

1. Initialize database tables:
   ```
   alembic upgrade head
   ```

</br>

5. Start the application in development mode:
   ```
   To start the development server, run:
  ```bash
  uvicorn app.main:app --reload
   ```
  In production use
  ```
  fastapi run
  ```
</br>

6. Test the application by making requests to endpoints.
   

## Deploy
YOU CAN DIRECTLY DEPLOY YOUR OWN VERSION USING THE LINK BELOW
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/CtmI_O?referralCode=e77QIa)


## 🤝 Contribute to the Project

We welcome contributions from the community to make this Behemoth FastAPI Starter Template even better. If you have ideas for improvements, new features, or bug fixes, feel free to:

- Fork the repository and create a new branch.
- Submit a Pull Request with your changes.
- Engage in discussions on ideas, enhancements, or fixes.

By contributing, you help make this template more valuable for developers building FastAPI applications. Together, we can create a robust foundation for large-scale projects. Thank you for your support!

For additional information, refer to the following resources:

- FastAPI documentation: https://fastapi.tiangolo.com/
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/
- Django Structure for Scale lecture: https://youtu.be/yG3ZdxBb1oo?si=D6A9dHyhKb_Kf-J7


## 📬 Contact

Feel free to reach out if you have questions or suggestions. I’m also open to consulting and tutoring opportunities. 😊

- Name: Bello Shehu Ango
- Email: angobello0@gmail.com
- GitHub: https://github.com/Grey-A
- Linkedin: https://linkedin.com/in/angobello0
- Upwork: https://www.upwork.com/freelancers/~01bb1007bf8311388a
- Instagram: https://www.instagram.com/bello_ango0/