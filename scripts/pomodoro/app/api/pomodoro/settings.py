from pydantic_settings import BaseSettings
from pydantic import BaseModel

class StorageModel(BaseModel):
    work_delta: int = 25
    break_delta: int = 5
    pause_start: int = 0
    end_time: int = 0
    is_work: bool = True
    is_paused: bool = False
    pomodoro_cnt: int = 0
    time_left: int = 0

class Settings(BaseSettings):
    work_delta: int = 25
    break_delta: int = 5
    port: int = 9999
    host: str = '0.0.0.0'

    class Config:
        env_prefix = 'POMODORO_'
        env_file = '../.env',
        env_file_encoding = 'utf-8'


settings = Settings()
