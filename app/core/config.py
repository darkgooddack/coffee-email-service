from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class KafkaConfig(BaseSettings):
    servers: str = "coffee_auth_kafka:9092"


class MailConfig(BaseSettings):
    username: str = "example@email.com"
    password: str = "your_mail_password"
    sender: EmailStr = "example@email.com"
    port: int = 465
    server: str = "smtp.yandex.ru"
    starttls: bool = False
    tls: bool = True
    from_name: str = "Coffee App"


class Settings(BaseSettings):
    kafka: KafkaConfig = KafkaConfig()
    mail: MailConfig = MailConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__"
    )


settings = Settings()
