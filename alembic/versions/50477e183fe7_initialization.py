"""initialization

Revision ID: 50477e183fe7
Revises: 
Create Date: 2024-04-24 14:59:31.327852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50477e183fe7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('age_range',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('age_min', sa.Integer(), nullable=False),
    sa.Column('age_max', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('dataset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hdx_id', sa.String(length=36), nullable=False),
    sa.Column('hdx_stub', sa.String(length=128), nullable=False),
    sa.Column('title', sa.String(length=1024), nullable=False),
    sa.Column('hdx_provider_stub', sa.String(length=128), nullable=False),
    sa.Column('hdx_provider_name', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hdx_id'),
    sa.UniqueConstraint('hdx_stub')
    )
    op.create_index(op.f('ix_dataset_hdx_provider_name'), 'dataset', ['hdx_provider_name'], unique=False)
    op.create_index(op.f('ix_dataset_hdx_provider_stub'), 'dataset', ['hdx_provider_stub'], unique=False)
    op.create_table('gender',
    sa.Column('code', sa.String(length=1), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('ipc_phase',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.CheckConstraint("code IN ('1', '2', '3', '4', '5', '3+', 'all')", name='ipc_phase_code'),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('ipc_type',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.CheckConstraint("code IN ('current', 'first projection', 'second projection')", name='ipc_phase_type'),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('hapi_updated_date', sa.DateTime(), nullable=False),
    sa.Column('hapi_replaced_date', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.CheckConstraint('(hapi_replaced_date IS NULL) OR (hapi_replaced_date >= hapi_updated_date)', name='hapi_dates'),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code', 'hapi_updated_date', name='code_date_unique2')
    )
    op.create_index(op.f('ix_location_hapi_replaced_date'), 'location', ['hapi_replaced_date'], unique=False)
    op.create_index(op.f('ix_location_hapi_updated_date'), 'location', ['hapi_updated_date'], unique=False)
    op.create_index(op.f('ix_location_reference_period_end'), 'location', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_location_reference_period_start'), 'location', ['reference_period_start'], unique=False)
    op.create_table('org_type',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_org_type_description'), 'org_type', ['description'], unique=False)
    op.create_table('population_group',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_population_group_description'), 'population_group', ['description'], unique=False)
    op.create_table('population_status',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_population_status_description'), 'population_status', ['description'], unique=False)
    op.create_table('sector',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_sector_name'), 'sector', ['name'], unique=False)
    op.create_table('admin1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_ref', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('is_unspecified', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('hapi_updated_date', sa.DateTime(), nullable=False),
    sa.Column('hapi_replaced_date', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.CheckConstraint('(hapi_replaced_date IS NULL) OR (hapi_replaced_date >= hapi_updated_date)', name='hapi_dates'),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.ForeignKeyConstraint(['location_ref'], ['location.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code', 'hapi_updated_date')
    )
    op.create_index(op.f('ix_admin1_hapi_replaced_date'), 'admin1', ['hapi_replaced_date'], unique=False)
    op.create_index(op.f('ix_admin1_hapi_updated_date'), 'admin1', ['hapi_updated_date'], unique=False)
    op.create_index(op.f('ix_admin1_reference_period_end'), 'admin1', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_admin1_reference_period_start'), 'admin1', ['reference_period_start'], unique=False)
    op.create_table('org',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('acronym', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('org_type_code', sa.String(length=32), nullable=True),
    sa.Column('reference_period_start', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('hapi_updated_date', sa.DateTime(), nullable=False),
    sa.Column('hapi_replaced_date', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.CheckConstraint('(hapi_replaced_date IS NULL) OR (hapi_replaced_date >= hapi_updated_date)', name='hapi_dates'),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.ForeignKeyConstraint(['org_type_code'], ['org_type.code'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_org_acronym'), 'org', ['acronym'], unique=False)
    op.create_index(op.f('ix_org_hapi_replaced_date'), 'org', ['hapi_replaced_date'], unique=False)
    op.create_index(op.f('ix_org_hapi_updated_date'), 'org', ['hapi_updated_date'], unique=False)
    op.create_index(op.f('ix_org_reference_period_end'), 'org', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_org_reference_period_start'), 'org', ['reference_period_start'], unique=False)
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset_ref', sa.Integer(), nullable=False),
    sa.Column('hdx_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('format', sa.String(length=32), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=False),
    sa.Column('download_url', sa.String(length=1024), nullable=False),
    sa.Column('is_hxl', sa.Boolean(), nullable=False),
    sa.Column('hapi_updated_date', sa.DateTime(), nullable=False),
    sa.Column('hapi_replaced_date', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.CheckConstraint('(hapi_replaced_date IS NULL) OR (hapi_replaced_date >= hapi_updated_date)', name='hapi_dates'),
    sa.ForeignKeyConstraint(['dataset_ref'], ['dataset.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('download_url'),
    sa.UniqueConstraint('hdx_id')
    )
    op.create_index(op.f('ix_resource_hapi_replaced_date'), 'resource', ['hapi_replaced_date'], unique=False)
    op.create_index(op.f('ix_resource_hapi_updated_date'), 'resource', ['hapi_updated_date'], unique=False)
    op.create_index(op.f('ix_resource_is_hxl'), 'resource', ['is_hxl'], unique=False)
    op.create_index(op.f('ix_resource_update_date'), 'resource', ['update_date'], unique=False)
    op.create_table('admin2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin1_ref', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('is_unspecified', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('hapi_updated_date', sa.DateTime(), nullable=False),
    sa.Column('hapi_replaced_date', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.CheckConstraint('(hapi_replaced_date IS NULL) OR (hapi_replaced_date >= hapi_updated_date)', name='hapi_dates'),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.ForeignKeyConstraint(['admin1_ref'], ['admin1.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code', 'hapi_updated_date', name='code_date_unique1')
    )
    op.create_index(op.f('ix_admin2_hapi_replaced_date'), 'admin2', ['hapi_replaced_date'], unique=False)
    op.create_index(op.f('ix_admin2_hapi_updated_date'), 'admin2', ['hapi_updated_date'], unique=False)
    op.create_index(op.f('ix_admin2_reference_period_end'), 'admin2', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_admin2_reference_period_start'), 'admin2', ['reference_period_start'], unique=False)
    op.create_table('food_security',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('ipc_phase_code', sa.String(length=32), nullable=False),
    sa.Column('ipc_type_code', sa.String(length=32), nullable=False),
    sa.Column('population_in_phase', sa.Integer(), nullable=False),
    sa.Column('population_fraction_in_phase', sa.Float(), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['ipc_phase_code'], ['ipc_phase.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['ipc_type_code'], ['ipc_type.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_food_security_population_fraction_in_phase'), 'food_security', ['population_fraction_in_phase'], unique=False)
    op.create_index(op.f('ix_food_security_population_in_phase'), 'food_security', ['population_in_phase'], unique=False)
    op.create_index(op.f('ix_food_security_reference_period_end'), 'food_security', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_food_security_reference_period_start'), 'food_security', ['reference_period_start'], unique=False)
    op.create_table('humanitarian_needs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('population_status_code', sa.String(length=32), nullable=True),
    sa.Column('population_group_code', sa.String(length=32), nullable=True),
    sa.Column('sector_code', sa.String(length=32), nullable=True),
    sa.Column('gender_code', sa.String(length=1), nullable=True),
    sa.Column('age_range_code', sa.String(length=32), nullable=True),
    sa.Column('disabled_marker', sa.Boolean(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.CheckConstraint('population >= 0', name='population'),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['age_range_code'], ['age_range.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['gender_code'], ['gender.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['population_group_code'], ['population_group.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['population_status_code'], ['population_status.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sector_code'], ['sector.code'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_humanitarian_needs_population'), 'humanitarian_needs', ['population'], unique=False)
    op.create_index(op.f('ix_humanitarian_needs_reference_period_end'), 'humanitarian_needs', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_humanitarian_needs_reference_period_start'), 'humanitarian_needs', ['reference_period_start'], unique=False)
    op.create_table('national_risk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('risk_class', sa.Integer(), nullable=False),
    sa.Column('global_rank', sa.Integer(), nullable=False),
    sa.Column('overall_risk', sa.Float(), nullable=False),
    sa.Column('hazard_exposure_risk', sa.Float(), nullable=False),
    sa.Column('vulnerability_risk', sa.Float(), nullable=False),
    sa.Column('coping_capacity_risk', sa.Float(), nullable=False),
    sa.Column('meta_missing_indicators_pct', sa.Float(), nullable=True),
    sa.Column('meta_avg_recentness_years', sa.Float(), nullable=True),
    sa.Column('reference_period_start', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.CheckConstraint('meta_avg_recentness_years >= 0.0', name='meta_avg_recentness_years'),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_national_risk_reference_period_end'), 'national_risk', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_national_risk_reference_period_start'), 'national_risk', ['reference_period_start'], unique=False)
    op.create_table('operational_presence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('org_ref', sa.Integer(), nullable=False),
    sa.Column('sector_code', sa.String(length=32), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['org_ref'], ['org.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sector_code'], ['sector.code'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operational_presence_reference_period_end'), 'operational_presence', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_operational_presence_reference_period_start'), 'operational_presence', ['reference_period_start'], unique=False)
    op.create_table('population',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('gender_code', sa.String(length=1), nullable=True),
    sa.Column('age_range_code', sa.String(length=32), nullable=True),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.CheckConstraint('(reference_period_end >= reference_period_start) OR (reference_period_start IS NULL)', name='reference_period'),
    sa.CheckConstraint('population >= 0', name='population'),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['age_range_code'], ['age_range.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['gender_code'], ['gender.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_population_population'), 'population', ['population'], unique=False)
    op.create_index(op.f('ix_population_reference_period_end'), 'population', ['reference_period_end'], unique=False)
    op.create_index(op.f('ix_population_reference_period_start'), 'population', ['reference_period_start'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_population_reference_period_start'), table_name='population')
    op.drop_index(op.f('ix_population_reference_period_end'), table_name='population')
    op.drop_index(op.f('ix_population_population'), table_name='population')
    op.drop_table('population')
    op.drop_index(op.f('ix_operational_presence_reference_period_start'), table_name='operational_presence')
    op.drop_index(op.f('ix_operational_presence_reference_period_end'), table_name='operational_presence')
    op.drop_table('operational_presence')
    op.drop_index(op.f('ix_national_risk_reference_period_start'), table_name='national_risk')
    op.drop_index(op.f('ix_national_risk_reference_period_end'), table_name='national_risk')
    op.drop_table('national_risk')
    op.drop_index(op.f('ix_humanitarian_needs_reference_period_start'), table_name='humanitarian_needs')
    op.drop_index(op.f('ix_humanitarian_needs_reference_period_end'), table_name='humanitarian_needs')
    op.drop_index(op.f('ix_humanitarian_needs_population'), table_name='humanitarian_needs')
    op.drop_table('humanitarian_needs')
    op.drop_index(op.f('ix_food_security_reference_period_start'), table_name='food_security')
    op.drop_index(op.f('ix_food_security_reference_period_end'), table_name='food_security')
    op.drop_index(op.f('ix_food_security_population_in_phase'), table_name='food_security')
    op.drop_index(op.f('ix_food_security_population_fraction_in_phase'), table_name='food_security')
    op.drop_table('food_security')
    op.drop_index(op.f('ix_admin2_reference_period_start'), table_name='admin2')
    op.drop_index(op.f('ix_admin2_reference_period_end'), table_name='admin2')
    op.drop_index(op.f('ix_admin2_hapi_updated_date'), table_name='admin2')
    op.drop_index(op.f('ix_admin2_hapi_replaced_date'), table_name='admin2')
    op.drop_table('admin2')
    op.drop_index(op.f('ix_resource_update_date'), table_name='resource')
    op.drop_index(op.f('ix_resource_is_hxl'), table_name='resource')
    op.drop_index(op.f('ix_resource_hapi_updated_date'), table_name='resource')
    op.drop_index(op.f('ix_resource_hapi_replaced_date'), table_name='resource')
    op.drop_table('resource')
    op.drop_index(op.f('ix_org_reference_period_start'), table_name='org')
    op.drop_index(op.f('ix_org_reference_period_end'), table_name='org')
    op.drop_index(op.f('ix_org_hapi_updated_date'), table_name='org')
    op.drop_index(op.f('ix_org_hapi_replaced_date'), table_name='org')
    op.drop_index(op.f('ix_org_acronym'), table_name='org')
    op.drop_table('org')
    op.drop_index(op.f('ix_admin1_reference_period_start'), table_name='admin1')
    op.drop_index(op.f('ix_admin1_reference_period_end'), table_name='admin1')
    op.drop_index(op.f('ix_admin1_hapi_updated_date'), table_name='admin1')
    op.drop_index(op.f('ix_admin1_hapi_replaced_date'), table_name='admin1')
    op.drop_table('admin1')
    op.drop_index(op.f('ix_sector_name'), table_name='sector')
    op.drop_table('sector')
    op.drop_index(op.f('ix_population_status_description'), table_name='population_status')
    op.drop_table('population_status')
    op.drop_index(op.f('ix_population_group_description'), table_name='population_group')
    op.drop_table('population_group')
    op.drop_index(op.f('ix_org_type_description'), table_name='org_type')
    op.drop_table('org_type')
    op.drop_index(op.f('ix_location_reference_period_start'), table_name='location')
    op.drop_index(op.f('ix_location_reference_period_end'), table_name='location')
    op.drop_index(op.f('ix_location_hapi_updated_date'), table_name='location')
    op.drop_index(op.f('ix_location_hapi_replaced_date'), table_name='location')
    op.drop_table('location')
    op.drop_table('ipc_type')
    op.drop_table('ipc_phase')
    op.drop_table('gender')
    op.drop_index(op.f('ix_dataset_hdx_provider_stub'), table_name='dataset')
    op.drop_index(op.f('ix_dataset_hdx_provider_name'), table_name='dataset')
    op.drop_table('dataset')
    op.drop_table('age_range')
    # ### end Alembic commands ###