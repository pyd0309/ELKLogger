# ELKLogging

## Installation

```
pip install ELKLogging
```

## Example

1. create instance

  * manual create
  ```
  from ELKLogging import *
  
  logger = Logger(logger_name='test_logger', log_level=logging.INFO)
  logger.set_message_data("service_name", "test_service")
  ```
  
  * using json config file
  ```
  from ELKLogging import *
  
  logger = Logger(config="logging.json")
  logger.set_message_data("service_name", "test_service")
  ```
  

