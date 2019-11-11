# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_druid_auth_py.py

Revision ID: e553e78e90c5
Revises: 18dc26817ad2
Create Date: 2019-02-01 16:07:04.268023

"""

# revision identifiers, used by Alembic.
revision = "e553e78e90c5"
down_revision = "18dc26817ad2"

import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import EncryptedType


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("clusters", sa.Column("broker_pass", EncryptedType(), nullable=True))
    op.add_column(
        "clusters", sa.Column("broker_user", sa.String(length=255), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("clusters", "broker_user")
    op.drop_column("clusters", "broker_pass")
    # ### end Alembic commands ###
