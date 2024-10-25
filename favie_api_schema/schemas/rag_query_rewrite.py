# rag query rewrite
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class RAGQueryRewriteRequest(BaseModel):
    class modelType(Enum):
        GPT_4O = "gpt-4o"
        CLAUDE_3_SONNET = "haiku"
        GPT_4O_MINI = "gpt-4o-mini"

    query: str
    model: Optional[modelType] = modelType.GPT_4O
    history_message: Optional[list[dict]] = None
    query_rewrite_prompt: Optional[str] = None


