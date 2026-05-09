# !/usr/bin/env python
# -*- coding: utf-8 -*-
# =====================================================
# @File   ：__init__.py
# @Date   ：2025/01/09 18:30
# @Author ：leemysw
# 2025/01/09 18:30   Create
# =====================================================
"""
[INPUT]: None
[OUTPUT]: 对外提供工具函数
[POS]: utils 模块入口
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""

from urllib.parse import quote

from feishu_docx.utils.config import get_config_dir, get_cache_dir
from feishu_docx.utils.progress import ProgressManager


def encode_md_link_path(path: str) -> str:
    """URL-encode each path segment for safe use in Markdown links.

    Splits on '/' so directory separators stay literal while spaces,
    Chinese characters, and other non-ASCII chars in filenames get
    percent-encoded.
    """
    return "/".join(quote(seg, safe="") for seg in path.split("/"))


__all__ = ["get_config_dir", "get_cache_dir", "ProgressManager", "encode_md_link_path"]

