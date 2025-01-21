from resolute.http._constants import *

def test_max_request_size():
	assert isinstance(MAX_REQUEST_SIZE, int) and MAX_REQUEST_SIZE > 0

def test_max_request_time():
	assert isinstance(MAX_REQUEST_TIME, float) and MAX_REQUEST_TIME > 0

def test_threads_per_core():
	assert isinstance(THREADS_PER_CORE, int) and THREADS_PER_CORE > 0
