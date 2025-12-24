from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.kafka.consumer import KafkaEmailConsumer
from app.core.logger import logger


kafka_consumer = KafkaEmailConsumer()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Kafka consumer...")
    await kafka_consumer.start()
    try:
        yield
    finally:
        logger.info("Stopping Kafka consumer...")
        await kafka_consumer.stop()

app = FastAPI(lifespan=lifespan)
