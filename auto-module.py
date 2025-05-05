from pathlib import Path


def create_module():
    """
    Automates the creation of a FastAPI module with necessary boilerplate
    """
    app_dir = Path("./app")

    if not app_dir.exists():
        print("App directory does not exist. Creating one...")
        app_dir.mkdir(parents=True)
        (app_dir / "__init__.py").touch()

    module = input("What is the module name? ").strip().title()
    module_path = app_dir / module

    if module_path.exists():
        print("Directory already exists.")
        return

    print(f"Creating the module: {module=}")
    module_path.mkdir()

    # Create subfolders and __init__.py files
    sub_folders = ["routes", "schemas"]
    for folder in sub_folders:
        sub_path = module_path / folder
        sub_path.mkdir()
        (sub_path / "__init__.py").touch()
        (sub_path / "base.py").touch()

    # Create specific schema files
    schema_files = ["create.py", "edit.py", "response.py"]
    schemas_path = module_path / "schemas"
    for schema_file in schema_files:
        (schemas_path / schema_file).touch()

    # Define files and templates
    files = [
        "__init__.py",
        "apis.py",
        "models.py",
        "services.py",
        "selectors.py",
        "exceptions.py",
        "formatters.py",
    ]

    file_templates = {
        "apis.py": f"""from fastapi import APIRouter

from app.core.tags import RouteTags
from app.{module}.routes.base import router as base_router

# Globals
router = APIRouter()
tags = RouteTags()

# Routes
router.include_router(base_router, prefix="/{module.lower()}s")
""",
        # Future example for services.py
        # "services.py": f"# Services for {module} module\n",
    }

    # Write or touch files
    for file in files:
        file_path = module_path / file
        content = file_templates.get(file)
        if content:
            file_path.write_text(content)
        else:
            file_path.touch()

    print(f"✅ Module '{module}' created successfully")


if __name__ == "__main__":
    create_module()
