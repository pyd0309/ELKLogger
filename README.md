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
   This decorator sends your message automatically to Logstash containing systemmetrics information. </br>
    If an error occurs you can send error_message or error_state to your method return. Then decorator set detail_message variable and send message to logstash.
    ```ruby
    from ELKLogging import *

    logger = Logger(config="logging.json")    

    @logger.wafer_logstash
    def test_wafer_logstash():
      try:
          [elem + elem ** 2 for elem in range(1, 10000)]
      except Exception:
          return logger.traceback_error()
    ```
  
  * Destination 
   
    You can select destination of log message even if your ELKLogging Object(ex.logger) has many handlers. 
    
    ```ruby
    logger.info("default : send logger.message to Logstash & File & Console")
    logger.info("send logger.message to Logstash", destination=[HANDLER.LOGSTASH])
    logger.info("send logger.message to File & Console", destination=[HANDLER.FILE, HANDLER.STREAM])
    logger.info("send logger.message to File", destination=[HANDLER.FILE])
    ```
  
  * Manual 
    ```ruby
    def test_logstash():
       try:
           logger.systemlog_tracing_start() # SystemMetrics trace start (cpu, mem, start_time)
           [elem + elem ** 2 for elem in range(1, 100000)]
           logger.systemlog_tracing_end() # SystemMetrics trace start (cpu, mem, end_time)
           logger.info("test_logstash") # Send to all Handler 
           raise
       except Exception:
           logger.set_message_data(key='detail_message', value=logger.traceback_error()) # If you "return logger.traceback_error()", don't have to set detail_message 
           logger.error("error occur test_logstash") # Send to all Handler 
    ```

    
    __output : File & Console__  
    ```
    [2022-08-24T04:05:57.295Z] [INFO] [test_service] [test_logstash] test_logstash
    [2022-08-24T04:05:57.312Z] [ERROR] [test_service] [test_logstash] error occur test_logstash
    ```
   
    __output : Logstash(Elasticsearch)__ 
    
    service_name | method | log_level | wafer_list | running_time | cpu_usage | mem_usage | message
    --- | --- | --- | --- | --- | --- | --- | --- | 
    test_service | test_logstash | INFO | ['test'] | 0.098 | 12.7 | 3.97 | [INFO] >> service_name : test_service, method : test_logstash, line_id : 0, process_id : 0, metro_ppid : 0, wafer_list : ['test'], cpu_usage : 12.7, mem_usage : 3.97, running_time : 0.09800505638122559, detail_message : test_logstash
    test_service | test_logstash | INFO | ['test'] | 0.098 | 12.7 | 3.97 | [ERROR] >> service_name : test_service, method : test_logstash, line_id : 0, process_id : 0, metro_ppid : 0, wafer_list : ['test'], cpu_usage : 12.7, mem_usage : 3.97, running_time : 0.09800505638122559, detail_message : Traceback (most recent call last): File "test.py", line 53, in test_logstash raise RuntimeError: No active exception to reraise
   
