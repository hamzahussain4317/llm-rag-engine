# from functools import lru_cache
# from pydantic_settings import BaseSettings
# from pydantic import Field

# class Settings(BaseSettings):
#     openai_api_key: str = Field(..., env="OPENAI_API_KEY")
#     openai_model: str = Field("gpt-4o-mini", env="OPENAI_MODEL")

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"

# @lru_cache
# def get_settings() -> Settings:
#     return Settings()
