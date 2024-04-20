run:
	uvicorn main:app --host 0.0.0.0

test_stream:
	python test_stream.py