import spdlog
import struct
import time

sinks = [
    spdlog.stdout_sink_st(),
    spdlog.tcp_sink_st("localhost", 12345, True),
]

logger = spdlog.SinkLogger("MyLogger", sinks)


def tcp_log(log_msg, level):
    jsonpattern = "{\"time\": \"%E\", " \
                  "\"name\": \"%n\", " \
                  "\"level\": \"%^%l%$\", " \
                  "\"process\": %P," \
                  "\"thread\": %t, " \
                  "\"message\": \"%v\"}"
    basic = "message: %v"
    pattern = jsonpattern
    logger.set_pattern(pattern)
    getattr(logger, level)(log_msg)


for i in range(10):
    tcp_log(f"msg: {i}", "info")
    # time.sleep(5)