import unittest
import time
from lib.utils.functools import MaxRetriesReachedError, call_delay, try_while, max_calls_per_second


class TestTryWhile(unittest.TestCase):

    def test_smoke(self):
        try_while(while_=lambda: False, sleep_time_s=0, max_retries=3)(
            lambda: None
        )()

    def test_simple(self):
        not_finished = True
        def finish():
            nonlocal not_finished
            not_finished = False

        try_while(while_=lambda: not_finished, sleep_time_s=0, max_retries=3)(
            finish
        )()

        not_finished = True
        with self.assertRaises(MaxRetriesReachedError):
            try_while(while_=lambda: not_finished, sleep_time_s=0, max_retries=3)(
                lambda: None
            )()


class TestCallDelay(unittest.TestCase):

    def test_smoke(self):
        _ = call_delay(seconds=0, minutes=0, hours=0)(lambda: None)

    def test_simple(self):
        f = call_delay(seconds=0.1)(lambda: None)
        start = time.time()
        f()
        f()
        end = time.time()
        self.assertTrue(0.1 <= end - start <= 0.2)


class TestMaxCallsPerSecond(unittest.TestCase):

    def test_smoke(self):
        _ = max_calls_per_second(1)(lambda: None)

    def test_simple(self):
        f = max_calls_per_second(10)(lambda: None)
        start = time.time()
        f()
        f()
        end = time.time()
        self.assertTrue(0.1 <= end - start <= 0.2)
