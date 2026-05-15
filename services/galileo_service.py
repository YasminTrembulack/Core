from typing import Set

from fastapi.logger import logger

from config import settings
from utils.http_client import get_request


class GalileoService:
    
    def get_unit_by_ids(self, ids: Set[str]):
        url = f"{settings.EXTERNAL_API_URL}?route=unidades"
        logger.info(f"User unit ids: {ids}")
        
        units = get_request(url)

        logger.info(f"User unit ids: {units[:10]}")
        
        return [
            unit
            for unit in units
            if str(unit.get("lojaId")) in ids
        ]