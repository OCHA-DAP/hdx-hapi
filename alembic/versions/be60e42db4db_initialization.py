"""Initialization

Revision ID: be60e42db4db
Revises: 
Create Date: 2023-09-20 12:43:26.000600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be60e42db4db'
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
    sa.Column('provider_code', sa.String(length=128), nullable=False),
    sa.Column('provider_name', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hdx_id'),
    sa.UniqueConstraint('hdx_stub')
    )
    op.create_index(op.f('ix_dataset_provider_code'), 'dataset', ['provider_code'], unique=False)
    op.create_index(op.f('ix_dataset_provider_name'), 'dataset', ['provider_name'], unique=False)
    op.create_table('gender',
    sa.Column('code', sa.CHAR(length=1), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('org_type',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('sector',
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_index(op.f('ix_sector_name'), 'sector', ['name'], unique=False)
    op.create_index(op.f('ix_sector_reference_period_start'), 'sector', ['reference_period_start'], unique=False)
    op.create_table('admin1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_ref', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('is_unspecified', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['location_ref'], ['location.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('org',
    sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('hdx_link', sa.String(length=1024), nullable=False),
    sa.Column('acronym', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('org_type_code', sa.String(length=32), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['org_type_code'], ['org_type.code'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_org_acronym'), 'org', ['acronym'], unique=False)
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
    sa.ForeignKeyConstraint(['dataset_ref'], ['dataset.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('download_url'),
    sa.UniqueConstraint('hdx_id')
    )
    op.create_index(op.f('ix_resource_is_hxl'), 'resource', ['is_hxl'], unique=False)
    op.create_index(op.f('ix_resource_update_date'), 'resource', ['update_date'], unique=False)
    op.create_table('admin2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin1_ref', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('is_unspecified', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['admin1_ref'], ['admin1.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('operational_presence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('org_ref', sa.Integer(), nullable=False),
    sa.Column('sector_code', sa.String(length=32), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['org_ref'], ['org.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sector_code'], ['sector.code'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operational_presence_reference_period_start'), 'operational_presence', ['reference_period_start'], unique=False)
    op.create_table('population',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_ref', sa.Integer(), nullable=False),
    sa.Column('admin2_ref', sa.Integer(), nullable=False),
    sa.Column('gender_code', sa.CHAR(length=1), nullable=True),
    sa.Column('age_range_code', sa.String(length=32), nullable=True),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('reference_period_start', sa.DateTime(), nullable=False),
    sa.Column('reference_period_end', sa.DateTime(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('source_data', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['admin2_ref'], ['admin2.id'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['age_range_code'], ['age_range.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['gender_code'], ['gender.code'], onupdate='CASCADE'),
    sa.ForeignKeyConstraint(['resource_ref'], ['resource.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_population_population'), 'population', ['population'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_population_population'), table_name='population')
    op.drop_table('population')
    op.drop_index(op.f('ix_operational_presence_reference_period_start'), table_name='operational_presence')
    op.drop_table('operational_presence')
    op.drop_table('admin2')
    op.drop_index(op.f('ix_resource_update_date'), table_name='resource')
    op.drop_index(op.f('ix_resource_is_hxl'), table_name='resource')
    op.drop_table('resource')
    op.drop_index(op.f('ix_org_reference_period_start'), table_name='org')
    op.drop_index(op.f('ix_org_acronym'), table_name='org')
    op.drop_table('org')
    op.drop_table('admin1')
    op.drop_index(op.f('ix_sector_reference_period_start'), table_name='sector')
    op.drop_index(op.f('ix_sector_name'), table_name='sector')
    op.drop_table('sector')
    op.drop_table('org_type')
    op.drop_table('location')
    op.drop_table('gender')
    op.drop_index(op.f('ix_dataset_provider_name'), table_name='dataset')
    op.drop_index(op.f('ix_dataset_provider_code'), table_name='dataset')
    op.drop_table('dataset')
    op.drop_table('age_range')
    # ### end Alembic commands ###
