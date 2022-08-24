# ELKLogging

## Installation

```
pip install ELKLogging
```

## Example

__1. Create instance__

  * manual create
  ```ruby
  from ELKLogging import *
  
  logger = Logger(logger_name='test_logger', log_level=LOG_LEVEL.INFO)
  logger.set_message_data("service_name", "test_service")
  logstash_handler = LogstashHandler(essential_key_list=['logstash_column1','logstash_column2'], host='127.0.0.1', port='8888')
                                 # Order of essential_key_list must be same as Logstash message format
  logstash_handler.setLevel(LOG_LEVEL.INFO)
  logger.addHandler(logstash_handler)
  ```
  
  * using json config file  
  ```ruby
  from ELKLogging import *
  
  logger = Logger(config="logging.json")    # json example : [logging.json](https://github.com/pyd0309/ELKLogging/blob/master/ELKLogging/logging.json)
  logger.set_message_data("service_name", "test_service")
  ```
  
__2. Send log message__
  
  

