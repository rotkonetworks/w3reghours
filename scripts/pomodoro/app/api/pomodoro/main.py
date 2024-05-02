import uvicorn
import datetime as dt
from dataclasses import asdict, dataclass, field
from enum import Enum
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from settings import settings, StorageModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@dataclass
class Storage:
    __add_to_dict__ = ['time_left']
    break_delta: int
    work_delta: int
    pause_start: int = 0
    end_time: int = field(init=False, repr=False)
    is_work: bool = True
    is_paused: bool = False
    pomodoro_cnt: int = 0

    def __post_init__(self):
        self.end_time = int(dt.datetime.now().timestamp()) + self.work_delta

    def _asdict(self):
        return {
                **asdict(self),
                **{a: getattr(self, a) for a in getattr(self, '__add_to_dict__', [])}}

    @property
    def time_left(self) -> int:
        now = int(dt.datetime.now().timestamp())
        if self.is_paused:
            return self.end_time - self.pause_start
        return self.end_time - now


class Variables(str, Enum):
    IS_WORK = 'is_work'
    IS_BREAK = 'is_break'
    IS_PAUSED = 'is_paused'
    TIME = 'end_time'
    PAUSE_START = 'pause_start'
    POMODORO_COUNT = 'pomodoro_count'


class Responses(str, Enum):
    LEFT = '{pomodoro} {minutes}:{seconds}'
    WORK_PERIOD_ENDED = 'take_break'
    BREAK_PERIOD_ENDED = 'break_over'
    PAUSE = 'PAUSE'
    NO_POMODORO = ''


_MINUTE = 60
storage = None

def init_database():
    global storage

    storage = Storage(
            work_delta=settings.work_delta*_MINUTE,
            break_delta=settings.break_delta*_MINUTE,
        )


@app.get('/new')
def new():
    init_database()
    return status.HTTP_200_OK


@app.get('/toggle')
def toggle():
    if storage is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active session")

    now = int(dt.datetime.now().timestamp())
    if storage.is_paused:
        # Calculate the total pause duration
        paused_duration = now - storage.pause_start
        storage.end_time += paused_duration
    else:
        storage.pause_start = now
    storage.is_paused = not storage.is_paused

    return status.HTTP_200_OK


@app.get('/time')
def time():

    if storage is None:
        return HTMLResponse(content=Responses.NO_POMODORO)

    if storage.is_paused:
        return HTMLResponse(content=Responses.PAUSE)

    if storage.end_time < int(dt.datetime.now().timestamp()):
        if storage.is_work:
            return HTMLResponse(content=Responses.WORK_PERIOD_ENDED)
        else:
            return HTMLResponse(content=Responses.BREAK_PERIOD_ENDED)

    time_left_in_seconds = storage.time_left
    return HTMLResponse(
        content=Responses.LEFT.value.format(
            pomodoro='🍅' * storage.pomodoro_cnt,
            minutes=time_left_in_seconds // 60,
            seconds=str(time_left_in_seconds % 60).zfill(2),
        ),
    )


@app.get('/next')
def next():
    if storage is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active session")

    now = int(dt.datetime.now().timestamp())
    storage.is_paused = False

    if storage.is_work:
        storage.pomodoro_cnt += 1
        storage.end_time = now + storage.break_delta
        storage.is_work = False
    else:
        storage.end_time = now + storage.work_delta
        storage.is_work = True

    return status.HTTP_200_OK


@app.get('/previous')
def previous():

    if storage is None or storage.pomodoro_cnt == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No previous session")

    now = int(dt.datetime.now().timestamp())
    storage.is_paused = False

    if storage.is_work:
        if storage.pomodoro_cnt > 0:
            storage.pomodoro_cnt -= 1
        storage.end_time = now + storage.break_delta
        storage.is_work = False
    else:
        storage.end_time = now + storage.work_delta
        storage.is_work = True

    return status.HTTP_200_OK


@app.get('/stop')
def stop():
    global storage
    storage = None
    return status.HTTP_200_OK


@app.get('/time&format=json', response_model=StorageModel)
def json():
    if not storage:
        return {}
    storage_dict = storage._asdict()
    storage_dict['time_left'] = storage.time_left
    return storage_dict


if __name__ == '__main__':
    uvicorn.run(
        app,
        port=settings.port,
        host=settings.host,
    )
