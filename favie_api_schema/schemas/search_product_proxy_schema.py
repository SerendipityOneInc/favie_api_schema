
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class SearchProductProxyRequest(BaseModel):
    """
    Search Product Proxy Request
    """
    query: str
    top_k: Optional[int] = 1
    source: Optional[str] = None
    ranker: Optional[str] = None
    site: Optional[str] = None
    direct_link: Optional[str] = "false"



class SearchProductProxyResponse(BaseModel):
    """
    Search Product Proxy Response
    """
    results: List[Dict[str, Any]]
    
    