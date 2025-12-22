from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.kafka.consumer import KafkaEmailConsumer


kafka_consumer = KafkaEmailConsumer()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_consumer.start()
    try:
        yield
    finally:
        await kafka_consumer.stop()

app = FastAPI(lifespan=lifespan)
