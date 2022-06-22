import os
from tarfile import SUPPORTED_TYPES


class BaseConfig:
    AUTH_TOKEN = os.getenv("AUTH_TOKEN", "dfdbc0292b2043e9a5fad8916f5c7e4d")
    SUPPORTED_FILES = [
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png",
        ".tif",
        ".tiff",
        ".docx",
        ".txt",
    ]
    QNA_APIs = [
        "https://api-inference.huggingface.co/models/deepset/minilm-uncased-squad2",
        "https://api-inference.huggingface.co/models/valhalla/longformer-base-4096-finetuned-squadv1",
        "https://api-inference.huggingface.co/models/aware-ai/roberta-large-squadv2"
    ]


class ProductionConfig(BaseConfig):
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")


class TestingConfig(BaseConfig):
    pass


class LocalConfig(BaseConfig):
    pass


env_config = {
    "production": ProductionConfig,
    "testing": TestingConfig,
    "local": LocalConfig,
}

CONFIG = env_config.get(os.getenv("ENV", "testing"), TestingConfig)
