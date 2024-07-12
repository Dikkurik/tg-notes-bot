from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    TOKEN: str
    USERS: list
    CHANNELS: list
    FILE_EXT: str
    NOTE_FOLDER: str
    IMG_FOLDER: str

    model_config = SettingsConfigDict(env_file=".env")

config = Config()
print(config.NOTE_FOLDER)