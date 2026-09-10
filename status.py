"""Helpers for building application status results."""

from __future__ import annotations

from typing import TypedDict


class StatusResult(TypedDict):
    status: str
    message: str


def build_status_result(message: str) -> StatusResult:
    """Build the standard successful application result."""
    return {"status": "ok", "message": message}
