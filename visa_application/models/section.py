from dataclasses import dataclass
from typing import List


@dataclass
class SectionItem:
    path: str = None
    text: str = None
    is_color: bool = False

    @classmethod
    def from_dict(cls, section_item_dict):
        return cls(
            path=section_item_dict.get("path", None),
            text=section_item_dict.get("text", None),
            is_color=section_item_dict.get("isColor", False),
        )


@dataclass
class Section:
    title: str
    items: List[SectionItem]

    @classmethod
    def from_dict(cls, section_dict):
        return cls(
            title=section_dict["title"],
            items=[
                SectionItem.from_dict(item_dict)
                for item_dict in section_dict["items"]
            ]
        )
