# rag自动化评测
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ContextRelevanceCompareResponse(BaseModel):
    query: Optional[str] = ""
    rewrite_query_1: Optional[dict] = None
    rewrite_query_2: Optional[dict] = None
    result: Optional[dict] = None

class ContextRelevanceRequest(BaseModel):

    class sourceType(Enum):
        """
        sourceType
        """

        HA3 = "ha3"
        GOOGLE = "google"

    class sourceTypeVersion(Enum):
        """
        sourceTypeVersion
        """

        VERSION_1 = "version_1"

    class searchType(Enum):
        """
        searchType
        """

        PRODUCT = "product"
        WEBPAGE = "webpage"

    class queryRewrite(Enum):
        """
        queryRewrite
        """

        VERSION_1 = "version_1"
        NO = "null"


class ContextRelevanceCompareRequest(BaseModel):
    query: Optional[str] = ""
    source_type_1: Optional[ContextRelevanceRequest.sourceType] = ContextRelevanceRequest.sourceType.HA3
    source_type_version_1: Optional[ContextRelevanceRequest.sourceTypeVersion] = ContextRelevanceRequest.sourceTypeVersion.VERSION_1
    search_type_1: Optional[ContextRelevanceRequest.searchType] = ContextRelevanceRequest.searchType.PRODUCT
    query_rewrite_1: Optional[ContextRelevanceRequest.queryRewrite] = ContextRelevanceRequest.queryRewrite.VERSION_1
    source_type_2: Optional[ContextRelevanceRequest.sourceType] = ContextRelevanceRequest.sourceType.GOOGLE
    source_type_version_2: Optional[ContextRelevanceRequest.sourceTypeVersion] = ContextRelevanceRequest.sourceTypeVersion.VERSION_1
    search_type_2: Optional[ContextRelevanceRequest.searchType] = ContextRelevanceRequest.searchType.PRODUCT
    query_rewrite_2: Optional[ContextRelevanceRequest.queryRewrite] = ContextRelevanceRequest.queryRewrite.NO
    top_k: Optional[int] = 1
    
class ContextRelevanceSingleRequest(BaseModel):
    query: Optional[str] = ""
    source_type: Optional[ContextRelevanceRequest.sourceType] = ContextRelevanceRequest.sourceType.HA3
    source_type_version: Optional[ContextRelevanceRequest.sourceTypeVersion] = ContextRelevanceRequest.sourceTypeVersion.VERSION_1
    search_type: Optional[ContextRelevanceRequest.searchType] = ContextRelevanceRequest.searchType.PRODUCT
    query_rewrite: Optional[ContextRelevanceRequest.queryRewrite] = ContextRelevanceRequest.queryRewrite.VERSION_1
    top_k: Optional[int] = 1


class ContextRelevanceSingleResponse(BaseModel):
    query: Optional[str] = ""
    rewrite_query: Optional[dict] = None
    result: Optional[list] = []

