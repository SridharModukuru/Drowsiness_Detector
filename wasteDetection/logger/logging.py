# dd/wasteDetection/logger/logging.py

import logging
import os
from datetime import datetime
from from_root import from_root

# Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Get the path to the root directory and append 'log' directory
log_dir = os.path.join(from_root(), 'log')

# Create the 'log' directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Complete path to the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Log a message to confirm logging is set up
logger.info("Logging setup is complete.")
