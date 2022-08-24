# ELKLogging

## Installation

```
pip install ELKLogging
```

## Example

__1. Create instance__

  * Manual
  ```ruby
  from ELKLogging import *
  
  logger = Logger(logger_name='test_logger', log_level=LOG_LEVEL.INFO)
  logger.set_message_data("service_name", "test_service")
  logstash_handler = LogstashHandler(essential_key_list=['logstash_column1','logstash_column2'], host='127.0.0.1', port='8888')
                                 # Order of essential_key_list must be same as Logstash message format
  logstash_handler.setLevel(LOG_LEVEL.INFO)
  logger.addHandler(logstash_handler)
  ```
  
  * Using json config file  (json example : [logging.json](https://github.com/pyd0309/ELKLogging/blob/master/ELKLogging/logging.json))
  ```ruby
  from ELKLogging import *
  
  logger = Logger(config="logging.json")    
  logger.set_message_data("service_name", "test_service")
  ```
  
  
__2. Send log message__
  
  * Decorator
    
    If you want to check your method __running time__, __cpu_usage__, __memory_usage__ then, you can use __@wafer_logstash__ decorator.
   This decorator sends your message automatically to Logstash containing systemmetrics information. 
    If an error occurs you can send error_message or error_state to your method return. Then decorator set detail_message variable and send message to logstash
  ```
  
  ```

