"""Initial migration

Revision ID: a545ae53105e
Revises: c7c0618e342b
Create Date: 2024-10-24 14:52:52.039635

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a545ae53105e'
down_revision = 'c7c0618e342b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('org_name', sa.String(length=100), nullable=False),
    sa.Column('org_url', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('profile_urls', sa.JSON(), nullable=True),
    sa.Column('contact_person', sa.JSON(), nullable=True),
    sa.Column('org_type', sa.String(length=50), nullable=True),
    sa.Column('verification_status', sa.String(length=20), nullable=True),
    sa.Column('cause_categories', postgresql.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('notification_preferences', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('volunteer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('occupation', sa.String(length=100), nullable=True),
    sa.Column('interests', postgresql.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('availability', sa.JSON(), nullable=True),
    sa.Column('skills', postgresql.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('profile_urls', sa.JSON(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('past_experience', sa.Text(), nullable=True),
    sa.Column('preferred_locations', postgresql.ARRAY(sa.String(length=100)), nullable=True),
    sa.Column('languages', postgresql.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('time_zone', sa.String(length=50), nullable=True),
    sa.Column('notification_preferences', sa.JSON(), nullable=True),
    sa.Column('certificates', postgresql.ARRAY(sa.String(length=100)), nullable=True),
    sa.Column('preferences', sa.JSON(), nullable=True),
    sa.Column('emergency_contact', sa.JSON(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opportunity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('required_skills', postgresql.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('duration_type', sa.String(length=20), nullable=True),
    sa.Column('opportunity_type', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('min_volunteers', sa.Integer(), nullable=True),
    sa.Column('max_volunteers', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('volunteer_match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('volunteer_id', sa.Integer(), nullable=False),
    sa.Column('opportunity_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('applied_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('volunteer_review', sa.Text(), nullable=True),
    sa.Column('volunteer_rating', sa.Float(), nullable=True),
    sa.Column('organization_review', sa.Text(), nullable=True),
    sa.Column('organization_rating', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['opportunity_id'], ['opportunity.id'], ),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('volunteer_match')
    op.drop_table('opportunity')
    op.drop_table('volunteer')
    op.drop_table('organization')
    # ### end Alembic commands ###