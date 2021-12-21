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
    # Using capnp for serialization
    # and augment capnp message with length within python.
    # No longer required.
    # msg = log_capnp.LogMsg.new_message()
    # msg.message = log_msg
    # msg.time = time.time()
    # msg_bytes = msg.to_bytes()
    # length = len(msg)
    # aug_msg = f"{struct.pack('i', length)}{msg}"
    # aug_msg = f"{length}{msg}"
    # logger.set_pattern("%v")
    # getattr(logger, level)(aug_msg)

    jsonpattern = "{\"time\": \"%E\", " \
                  "\"name\": \"%n\", " \
                  "\"level\": \"%^%l%$\", " \
                  "\"process\": %P," \
                  "\"thread\": %t, " \
                  "\"message\": \"%v\"}"
    logger.set_pattern(jsonpattern)
    getattr(logger, level)(log_msg)

    # logger.set_pattern("%v")
    # getattr(logger, level)(log_msg)


tcp_log("test2", "info")

