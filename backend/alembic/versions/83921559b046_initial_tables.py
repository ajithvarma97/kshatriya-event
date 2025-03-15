"""Initial tables

Revision ID: 83921559b046
Revises: 
Create Date: 2025-03-15 22:03:36.772863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83921559b046'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sponsor',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('tier', sa.Enum('platinum', 'gold', 'silver', 'bronze', name='sponsortier'), nullable=False),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('contact_name', sa.String(), nullable=True),
    sa.Column('contact_email', sa.String(), nullable=True),
    sa.Column('contact_phone', sa.String(), nullable=True),
    sa.Column('amount_paid', sa.Float(), nullable=True),
    sa.Column('payment_status', sa.Enum('pending', 'partial', 'paid', name='paymentstatus'), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sponsor_id'), 'sponsor', ['id'], unique=False)
    op.create_index(op.f('ix_sponsor_name'), 'sponsor', ['name'], unique=False)
    op.create_index(op.f('ix_sponsor_tier'), 'sponsor', ['tier'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_sponsor_tier'), table_name='sponsor')
    op.drop_index(op.f('ix_sponsor_name'), table_name='sponsor')
    op.drop_index(op.f('ix_sponsor_id'), table_name='sponsor')
    op.drop_table('sponsor')
    # ### end Alembic commands ### 