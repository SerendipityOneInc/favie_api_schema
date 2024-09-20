"""
image search schemas
"""
from typing import Optional

from pydantic import BaseModel


class ImageSearchRequest(BaseModel):
    """
    Image Search Request
    """

    image_url: str



class ImageSearchResponse(BaseModel):
    """
    Image Search Response
    """

    image_url: Optional[str] = None
    bbox: Optional[list[list[int]]] = None

    