from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    MONGO_URI: str
    #MONGO_CONNECTION_STRING: str
    MONGO_DB: str
    
    # Configuración de la aplicación
    APP_NAME: str = Field(
        default="API del Hospital BDR", 
        description="Nombre de la aplicación"
    )
    APP_VERSION: str = Field(
        default="1.0.0", 
        description="Versión de la aplicación"
    )
    
    # Configuración de CORS
    ALLOWED_ORIGINS: List[str] = Field(
        default=["*"], 
        description="Orígenes permitidos para CORS"
    )
    
settings = Settings()