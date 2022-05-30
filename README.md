# SWA_hm_Kukhar

running services:
uvicorn facade_service:app --reload --port=8000
uvicorn logging_service:app --reload --port=8001
uvicorn message_service:app --reload --port=8002
