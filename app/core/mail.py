from fastapi_mail import FastMail, ConnectionConfig
from app.core.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail.username,
    MAIL_PASSWORD=settings.mail.password,
    MAIL_FROM=settings.mail.sender,
    MAIL_PORT=settings.mail.port,
    MAIL_SERVER=settings.mail.server,
    MAIL_STARTTLS=settings.mail.starttls,
    MAIL_SSL_TLS=settings.mail.tls,
    MAIL_FROM_NAME=settings.mail.from_name,
)


fm = FastMail(conf)
