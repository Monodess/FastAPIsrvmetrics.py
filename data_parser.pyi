from sqlalchemy import create_engine

import data_capturer as dc
import sqlalchemy as sa
import pydantic as pd

# to create engine will its
# to open a connection without commiting it use ENGINE.connect()
#
engine = create_engine()
engine.connect()



