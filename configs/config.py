import os

# Configuration for the Trend Agent Space

class Config:
    def __init__(self):
        self.trend_service_url = os.environ.get('TREND_SERVICE_URL')
        self.data_ingestion_service_url = os.environ.get('DATA_INGESTION_SERVICE_URL')
        self.data_processing_service_url = os.environ.get('DATA_PROCESSING_SERVICE_URL')