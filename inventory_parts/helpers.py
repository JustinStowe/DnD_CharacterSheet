"""
Inventory helper functions for content management moved out of the UI module.
"""

from typing import Dict, Any, List


def normalize_item_schema(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'name': item.get('name', ''),
        'weight': float(item.get('weight', 0.0) or 0.0),
        'quantity': int(item.get('quantity', 1) or 1),
        'notes': item.get('notes', ''),
        'is_container': bool(item.get('is_container', False)),
        'capacity_lbs': float(item.get('capacity_lbs', 0.0) or 0.0),
        'count_contents_toward_carry': bool(item.get('count_contents_toward_carry', True)),
        'contents': item.get('contents', []).copy() if item.get('contents') else []
    }


def add_content_to_container(container_item: Dict[str, Any], content_item: Dict[str, Any]) -> bool:
    if not container_item.get('is_container'):
        return False
    cap = container_item.get('capacity_lbs', 0.0) or 0.0
    if cap > 0:
        current = sum(c.get('weight', 0) * c.get('quantity', 1) for c in container_item.get('contents', []))
        new_total = current + (content_item.get('weight', 0) * content_item.get('quantity', 1))
        if new_total > cap:
            return False
    normalized = normalize_item_schema(content_item)
    container_item.setdefault('contents', []).append(normalized)
    return True


def edit_content_in_container(container_item: Dict[str, Any], index: int, new_content: Dict[str, Any]) -> bool:
    if not container_item.get('is_container'):
        return False
    contents = container_item.get('contents', [])
    if not (0 <= index < len(contents)):
        return False
    cap = container_item.get('capacity_lbs', 0.0) or 0.0
    if cap > 0:
        existing = sum(c.get('weight', 0) * c.get('quantity', 1) for i, c in enumerate(contents) if i != index)
        new_total = existing + (new_content.get('weight', 0) * new_content.get('quantity', 1))
        if new_total > cap:
            return False
    contents[index] = normalize_item_schema(new_content)
    return True


def remove_content_from_container(container_item: Dict[str, Any], index: int) -> bool:
    contents = container_item.get('contents', [])
    if not (0 <= index < len(contents)):
        return False
    contents.pop(index)
    return True
