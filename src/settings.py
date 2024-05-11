from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    universities_etl_pipeline_name: str = "ETL"
    # FIXME: replace to "0 3 * * *"
    etl_pipeline_schedule: str = "*/20 * * * * *"
