from dataclasses import dataclass
from typing import List

@dataclass
class EbayItem:
    item_id: int
    title: str
    category_id: int
    category_name: str
    current_price: float
    bid_count: int
    item_details: dict
    item_description:str
    images: List[str]
    feedback_score: float
    positive_feedback_percent: float

    
