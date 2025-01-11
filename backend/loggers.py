import logging


def get_chat_logger(name='chat-app-logger'):
    """
    Create and configure a logger for the chat application.

    The logger is initialized with a default name and configured to output logs
    with a standardized format and INFO level of logging. The implementation uses the
    Python logging library, but can be extended to integrate with centralized logging
    solutions such as Splunk, Datadog, or the ELK stack.

    Args:
        name (str): Name of the logger. Defaults to 'chat-app-logger'.

    Returns:
        logging.Logger: Configured logger instance.

    Note:
        - The `logging.basicConfig` sets a simple configuration for logging;
          this should be replaced in production with a centralized logging system.
        - Centralized logging solutions can use libraries or log shippers such as:
            - **Splunk**: Use the `SplunkHandler` from the `splunk_logging` library
              to forward logs to Splunk.
            - **Fluentd/Filebeat**: Forward logs to ELK/other tools.
    """

    # Configure the basic logging settings: log level, format, and timestamp format.
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Get or create a logger with the specified name.
    logger = logging.getLogger(name)

    # Centralized logging integration example (commented out for now):
    # Uncomment and configure for production usage.
    # from splunk_logging import SplunkHandler
    # splunk_handler = SplunkHandler(
    #     host="splunk-server-url",
    #     port=8088,
    #     token="your-splunk-token",
    # )
    # logger.addHandler(splunk_handler)

    return logger