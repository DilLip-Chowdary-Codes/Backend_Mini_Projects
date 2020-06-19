from dataclasses import dataclass

@dataclass
class FormDto:
    form_id: int
    title: str
    is_live: bool
