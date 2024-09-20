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
    top_k: Optional[int] = 1



class ImageSearchResponse(BaseModel):
    """
    Image Search Response
    """

    image_url: Optional[list[str]] = None

    