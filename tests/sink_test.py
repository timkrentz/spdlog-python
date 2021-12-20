import capnp
import funcy
import log_capnp
import spdlog
import struct
import time
import os

sinks = [
    spdlog.stdout_sink_st(),
    spdlog.stdout_sink_mt(),
    spdlog.stderr_sink_st(),
    spdlog.stderr_sink_mt(),
    spdlog.daily_file_sink_st("DailySinkSt.log", 0, 0),
    spdlog.daily_file_sink_mt("DailySinkMt.log", 0, 0),
    spdlog.rotating_file_sink_st("RotSt.log", 1024, 1024),
    spdlog.rotating_file_sink_mt("RotMt.log", 1024, 1024),
    spdlog.tcp_sink_st("localhost", 12345, False),
    spdlog.tcp_sink_mt("localhost", 12345, False)
]


# d = msg.to_dict()
# print(d)
# msg_bytes = msg.to_bytes()

# msg_chunks = list(funcy.chunks(8, msg_bytes))

logger = spdlog.SinkLogger("Hello", sinks)
#

def tcp_log(log_msg, level):
    msg = log_capnp.LogMsg.new_message()
    msg.message = log_msg
    msg.time = time.time()
    msg_bytes = msg.to_bytes()

    # length = len(msg)
    # aug_msg = f"{struct.pack('i', length)}{msg}"
    # aug_msg = f"{length}{msg}"
    logger.set_pattern("%v")
    # jsonpattern = "{\"time\": \"%E\", " \
    #               "\"name\": \"%n\", " \
    #               "\"level\": \"%^%l%$\", " \
    #               "\"process\": %P," \
    #               "\"thread\": %t, " \
    #               "\"message\": \"%v\"}"
    # logger.set_pattern(jsonpattern)
    getattr(logger, level)(msg_bytes)


tcp_log("test", "info")

# logger.info("hemlo")

#
# # Set up the opening brace and an array named "log"
# # we're setting a global format here but as per the docs you can set this on an individual log as well
#
# spdlog::set_pattern(set_pattern("{\n \"log\": [");
# auto mylogger = spdlog::basic_logger_mt("json_logger", "mylog.json");
# mylogger->info("");//this initializes the log file with the opening brace and the "log" array as above
# # We have some extra formatting on the log level %l below to keep color coding when dumping json to the console and we use a full ISO 8601 time/date format
# std::string jsonpattern = {"{\"time\": \"%Y-%m-%dT%H:%M:%S.%f%z\", \"name\": \"%n\", \"level\": \"%^%l%$\", \"process\": %P, \"thread\": %t, \"message\": \"%v\"},"};
# spdlog::set_pattern(jsonpattern);
#
# logger.info(msg_bytes)
