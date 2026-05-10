from typing import Dict, List, Optional

_registry: Dict[str, List[float]] = {}

def set_importance(req_id: str, importance: List[float]) -> None:
    _registry[req_id] = importance

def pop_importance(req_id: str) -> Optional[List[float]]:
    return _registry.pop(req_id, None)