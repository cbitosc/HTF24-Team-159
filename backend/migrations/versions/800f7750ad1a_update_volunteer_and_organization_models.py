"""Update volunteer and organization models

Revision ID: 800f7750ad1a
Revises: a545ae53105e
Create Date: 2024-10-27 01:17:08.378347

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '800f7750ad1a'
down_revision = 'a545ae53105e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('organization', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('contact_name', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('contact_email', sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.drop_constraint('organization_id_fkey', type_='foreignkey')
        batch_op.drop_column('notification_preferences')
        batch_op.drop_column('verification_status')
        batch_op.drop_column('contact_person')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.drop_column('city')
        batch_op.drop_column('role')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')
        batch_op.drop_column('country')

    with op.batch_alter_table('volunteer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.drop_constraint('volunteer_id_fkey', type_='foreignkey')
        batch_op.drop_column('preferences')
        batch_op.drop_column('notification_preferences')
        batch_op.drop_column('emergency_contact')
        batch_op.drop_column('interests')
        batch_op.drop_column('preferred_locations')
        batch_op.drop_column('gender')
        batch_op.drop_column('occupation')
        batch_op.drop_column('time_zone')
        batch_op.drop_column('past_experience')
        batch_op.drop_column('age')
        batch_op.drop_column('languages')
        batch_op.drop_column('certificates')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('volunteer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('certificates', postgresql.ARRAY(sa.VARCHAR(length=100)), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('languages', postgresql.ARRAY(sa.VARCHAR(length=50)), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('past_experience', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('time_zone', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('occupation', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('gender', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('preferred_locations', postgresql.ARRAY(sa.VARCHAR(length=100)), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('interests', postgresql.ARRAY(sa.VARCHAR(length=50)), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('emergency_contact', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('notification_preferences', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('preferences', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('volunteer_id_fkey', 'user', ['id'], ['id'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('created_at')
        batch_op.drop_column('profile_picture')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('name')
        batch_op.drop_column('password')
        batch_op.drop_column('email')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('city', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.drop_column('name')

    with op.batch_alter_table('organization', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact_person', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('verification_status', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('notification_preferences', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('organization_id_fkey', 'user', ['id'], ['id'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('contact_email')
        batch_op.drop_column('contact_name')
        batch_op.drop_column('created_at')
        batch_op.drop_column('password')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
