import asyncio
import json
from aiokafka import AIOKafkaConsumer
from app.service.email import send_verification_email_message
from app.schema.events import EmailVerificationSendCommand
from app.core.config import settings


class KafkaEmailConsumer:
    def __init__(self):
        self._consumer: AIOKafkaConsumer | None = None
        self._task: asyncio.Task | None = None

    async def start(self):
        self._consumer = AIOKafkaConsumer(
            "email.send.verification",
            bootstrap_servers=[settings.kafka_servers],
            group_id="email-service",
            enable_auto_commit=False,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )
        await self._consumer.start()
        self._task = asyncio.create_task(self._consume())

    async def stop(self):
        if self._task:
            self._task.cancel()
        if self._consumer:
            await self._consumer.stop()

    async def _consume(self):
        try:
            async for message in self._consumer:
                payload = message.value
                cmd = EmailVerificationSendCommand(**payload)
                await send_verification_email_message(cmd)
                await self._consumer.commit()
        except asyncio.CancelledError:
            pass
