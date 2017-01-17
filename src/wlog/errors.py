#!/usr/bin/env python
"""Provide error classes for wlog."""

# Imports


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"




class WlogError(Exception):

    """Base error class for wlog."""


class ValidationError(WlogError):

    """Raise when a validation/sanity check comes back with unexpected value."""
