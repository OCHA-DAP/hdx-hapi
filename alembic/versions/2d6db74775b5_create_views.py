"""create views

Revision ID: 2d6db74775b5
Revises: 927d2ce143cc
Create Date: 2024-04-25 15:02:49.678672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from hapi_schema.db_admin1 import view_params_admin1
from hapi_schema.db_admin2 import view_params_admin2
from hapi_schema.db_age_range import view_params_age_range
from hapi_schema.db_dataset import view_params_dataset
from hapi_schema.db_food_security import view_params_food_security
from hapi_schema.db_gender import view_params_gender
from hapi_schema.db_humanitarian_needs import view_params_humanitarian_needs
from hapi_schema.db_ipc_phase import view_params_ipc_phase
from hapi_schema.db_ipc_type import view_params_ipc_type
from hapi_schema.db_location import view_params_location
from hapi_schema.db_national_risk import view_params_national_risk
from hapi_schema.db_operational_presence import view_params_operational_presence
from hapi_schema.db_org import view_params_org
from hapi_schema.db_org_type import view_params_org_type
from hapi_schema.db_population import view_params_population
from hapi_schema.db_population_group import view_params_population_group
from hapi_schema.db_population_status import view_params_population_status
from hapi_schema.db_resource import view_params_resource
from hapi_schema.db_sector import view_params_sector

from hdx_hapi.db.models.views.util.util import CreateView, DropView


# revision identifiers, used by Alembic.
revision: str = '2d6db74775b5'
down_revision: Union[str, None] = '927d2ce143cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


VIEW_LIST = [
    view_params_admin1,
    view_params_admin2,
    view_params_age_range,
    view_params_dataset,
    view_params_food_security,
    view_params_gender,
    view_params_humanitarian_needs,
    view_params_ipc_phase,
    view_params_ipc_type,
    view_params_location,
    view_params_national_risk,
    view_params_operational_presence,
    view_params_org_type,
    view_params_org,
    view_params_population_group,
    view_params_population_status,
    view_params_population,
    view_params_resource,
    view_params_sector,
]


def upgrade() -> None:
    for v in VIEW_LIST:
        op.get_bind().execute(CreateView(v.name, v.selectable))


def downgrade() -> None:
    for v in VIEW_LIST:
        op.get_bind().execute(DropView(v.name))
