
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class SearchProductProxyRequest(BaseModel):
    """
    Search Product Proxy Request
    """
    user_id: Optional[str] = ""
    task_id: Optional[str] = ""
    query: str
    top_k: Optional[int] = 1
    source: Optional[str] = None
    ranker: Optional[str] = None
    budget: Optional[str] = "0"
    brand: Optional[str] = None
    site: Optional[str] = None
    direct_link: Optional[str] = "false"
    filters: Optional[dict] = None
    ha3_contain_sites: Optional[list[str]] = None
    ha3_nocontain_sites: Optional[list[str]] = None
    models: Optional[list[str]] = None
    use_internal_LLM: Optional[bool] = False
    search_type: Optional[str] = "text"


class SearchProductProxyResponse(BaseModel):
    """
    Search Product Proxy Response
    """
    results: List[Dict[str, Any]]
    
    