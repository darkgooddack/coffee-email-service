from fastapi_mail import MessageSchema, MessageType

from app.core.mail import fm
from app.schema.events import EmailVerificationSendCommand


async def send_verification_email_message(
    command: EmailVerificationSendCommand
):
    message = MessageSchema(
        subject="Подтверждение почты",
        recipients=[command.email],
        body=(
            "Ваш код подтверждения: {code}.\n"
            "Поторопитесь, через 5 минут он перестанет работать."
        ).format(code=command.code),
        subtype=MessageType.html,
    )
    await fm.send_message(message)
