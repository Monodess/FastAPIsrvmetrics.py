import operator

# Mapping string keys to SQLAlchemy-compatible methods
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


