import logging
import os


# =========================================================
# LOG DIRECTORY
# =========================================================

LOG_DIR = "logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)


# =========================================================
# LOG FILE
# =========================================================

LOG_FILE = os.path.join(
    LOG_DIR,
    "log.txt"
)


# =========================================================
# LOGGER
# =========================================================

logger = logging.getLogger(
    "employee_api"
)

logger.setLevel(
    logging.INFO
)


# Prevent duplicate logs
if not logger.handlers:

    # -----------------------------------------------------
    # FILE HANDLER
    # -----------------------------------------------------

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setLevel(
        logging.INFO
    )

    # -----------------------------------------------------
    # CONSOLE HANDLER
    # -----------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(
        logging.INFO
    )

    # -----------------------------------------------------
    # LOG FORMAT
    # -----------------------------------------------------

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)