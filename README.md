# ELKLogging

## Installation

```
pip install ELKLogging
```

## Example

__1. create instance__

  * manual create
  ```ruby
  from ELKLogging import *
  
  logger = Logger(logger_name='test_logger', log_level=logging.INFO)
  logger.set_message_data("service_name", "test_service")
  ```
  
  * using json config file  
  json example : [logging.json](https://github.com/pyd0309/ELKLogging/blob/master/ELKLogging/logging.json)
  ```ruby
  from ELKLogging import *
  
  logger = Logger(config="logging.json")
  logger.set_message_data("service_name", "test_service")
  ```
  
  

