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
    logger.set_message_data("wafer_list", ["test"])
    
    #logstash
    logstash_handler = LogstashHandler(essential_key_list=['logstash_column1','logstash_column2'], host='127.0.0.1', port='8888')
                                   # Order of essential_key_list must be same as Logstash message format
    logstash_handler.setLevel(LOG_LEVEL.INFO)
    logger.add_handler(logstash_handler)
    
    #file
    fmt = "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s] %(message)s"
    file_handler = FileStreamHandler(folder_path='./folder1/folder2', file_name="mp_log.txt", encoding='UTF-8',
                                 maxBytes=20 * 1024 * 1024, backupCount=14, fmt=fmt)
    file_handler.setLevel(LOG_LEVEL.INFO)
    logger.add_handler(file_handler)
  
    #stream
    fmt = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    stream_handler = ConsoleStreamHandler(fmt=fmt)
    stream_handler.setLevel(LOG_LEVEL.INFO)
    logger.add_handler(stream_handler)
    ```
  
  * Using json config file  (json example : [logging.json](https://github.com/pyd0309/ELKLogging/blob/master/ELKLogging/logging.json))
    ```ruby
    #main.py
    
    import json
    from ELKLogging import *

    with open("logging.json", "r", encoding='utf-8') as file:
        config_data = json.load(file)
    logger = Logger(config=config_data)
    logger.set_message_data("wafer_list", ["test"])
    
    #test.py (useless to create object -> use Logger() because it is created by singletone pattern)
    
    from ELKLogging import *

    def test_method():
        Logger().info("test_method")
    ```
    
  * config file path in parent directory
    ```ruby
    from pathlib import Path
    import json

    log_dir = os.path.join(Path(os.path.dirname(__file__)).parent, 'logging.json')
    with open(log_dir, "r", encoding='utf-8') as file:
        config_data = json.load(file)

    ```
  
  
__2. Send log message__
  
  * Decorator
    
    If you want to check your method __running time__, __cpu_usage__, __memory_usage__ then, you can use __@wafer_logstash__ decorator.
   This decorator sends your message automatically to Logstash containing systemmetrics information. </br>
    If an error occurs you can send error_message or error_state to your method return. Then decorator set message variable and send it to logstash.
    ```ruby
    from ELKLogging import *

    with open("logging.json", "r", encoding='utf-8') as file:
        config_data = json.load(file)
    logger = Logger(config=config_data)
    logger.set_message_data("wafer_list", ["test"])

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
           logger.error(message=logger.traceback_error(), destination=[HANDLER.LOGSTASH])
           logger.error(message="error occur test_logstash", destination=[HANDLER.FILE, HANDLER.STREAM])
           
           #if all the handlers recive same message, then you can change code below
           #logger.error("error occur test_logstash")
    ```

    
    __output : File & Console__  
    ```
    [2022-08-24T04:05:57.295Z] [INFO] [test_service] [test_logstash] test_logstash
    [2022-08-24T04:05:57.312Z] [ERROR] [test_service] [test_logstash] error occur test_logstash
    ```
   
    __output : Logstash(Elasticsearch)__ 
    
    service_name | method | log_level | wafer_list | running_time | cpu_usage | mem_usage | message
    --- | --- | --- | --- | --- | --- | --- | --- | 
    test_service | test_logstash | INFO | ['test'] | 0.098 | 12.7 | 3.97 | [INFO] >> service_name : test_service, method : test_logstash, line_id : 0, process_id : 0, metro_ppid : 0, wafer_list : ['test'], cpu_usage : 12.7, mem_usage : 3.97, running_time : 0.098, detail_message : test_logstash
    test_service | test_logstash | INFO | ['test'] | 0.098 | 12.7 | 3.97 | [ERROR] >> service_name : test_service, method : test_logstash, line_id : 0, process_id : 0, metro_ppid : 0, wafer_list : ['test'], cpu_usage : 12.7, mem_usage : 3.97, running_time : 0.098, detail_message : Traceback (most recent call last): File "test.py", line 53, in test_logstash raise RuntimeError: No active exception to reraise
   
