"""Operator mapping for database filtering operations.

This module provides a mapping of string operator representations to SQLAlchemy
compatible filter methods, allowing flexible query construction.
"""
import operator

# Mapping string keys to SQLAlchemy-compatible filter methods
OPERATORS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "!=": operator.ne,
    "=": operator.eq,
    "like": lambda attr, val: attr.like(val),
    "in": lambda attr, val: attr.in_(val)
}


