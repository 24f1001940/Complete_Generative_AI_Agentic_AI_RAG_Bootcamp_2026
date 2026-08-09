"""
Lecture 38: Complete Python Logging Guide: From Basics to Production
Author: MOHD SAQIB
"""
import logging
import sys
from pathlib import Path

def setup_production_logger(name: str = "ai_app") -> logging.Logger:
    """Configures a multi-handler logger for console output and log files."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers if logger is re-initialized
    if logger.handlers:
        return logger

    # Formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler (INFO level)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File Handler (DEBUG level)
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "app.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    logger = setup_production_logger("RAGPipeline")

    logger.debug("Debugging vector similarity search calculations...")
    logger.info("Initializing LLM provider client: gpt-4o")
    logger.warning("Token count approaching max context window threshold (85% capacity)")
    logger.error("Failed to fetch chunk from vector store: Connection timed out")