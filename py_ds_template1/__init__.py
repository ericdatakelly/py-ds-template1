import logging
import os
from pathlib import Path

from dotenv import load_dotenv

# Create project constants
PROJECT_DIR = Path.cwd().resolve()
USER_HOME = Path.home().resolve()

# Setup logging (import the logger in any project file and use it to log messages)
logger = logging.getLogger("py-ds-template1")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(Path(PROJECT_DIR, "logs", "py_ds_template1.log"))
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Get environment variables from a .env file
load_dotenv()
ENV_VAR = os.getenv("ENV_VAR")
