[loggers]
keys=root

[handlers]
keys=consoleHandler, fileHandler, jsonFileHandler

[formatters]
keys=simpleFormatter, jsonFormatter

[logger_root]
level=${LOG_LEVEL}
handlers=consoleHandler, fileHandler, jsonFileHandler


[handler_consoleHandler]
class=StreamHandler
level=${LOG_LEVEL_CONSOLE}
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class = FileHandler
args = ('/var/log/hapi/hapi.log','a')
level = ${LOG_LEVEL_TXT}
formatter = simpleFormatter

[handler_jsonFileHandler]
class = FileHandler
args = ('/var/log/hapi/hapi-json.log','a')
level = ${LOG_LEVEL_JSON}
formatter = jsonFormatter

[formatter_simpleFormatter]
format=[%(process)d - %(thread)d] %(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)d] %(message)s
datefmt=

[formatter_jsonFormatter]
format = %(process)d %(thread)d %(asctime)s %(levelname) %(threadName)s %(name)s %(lineno)d %(message)s %(funcName)s
class = pythonjsonlogger.jsonlogger.JsonFormatter
