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
    embed_model: Optional[str] = "v2/base-Epoch_36.pt"



class ImageSearchResponse(BaseModel):
    """
    Image Search Response
    """

    class ImageDetail(BaseModel):
        
        """
        Image detail
        """

        image_url: Optional[list[str]] = None
        bbox: Optional[list[int]] = None
        score: Optional[list[str]] = None
    
    image_list: Optional[list[ImageDetail]] = None
    