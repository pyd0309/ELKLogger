# ELKLogging

## Installation

```
pip install ELKLogging
```

## Example

1. create instance

  * manual create
      
  * using json config file
  ```
  from ELKLogging import *
  
  logger = Logger(config="logging.json")
  logger.set_message_data("wafer_list", ["test"])
  logger.set_message_data("service_name", "test_service")
  ```
  

