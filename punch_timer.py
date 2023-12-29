import time


def punch_in():
    return time.perf_counter_ns()


def punch_out():
    return time.perf_counter_ns()


def punch_diff(start_time, end_time):
    return end_time - start_time
