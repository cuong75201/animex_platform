from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index
from sqlmodel import Field, SQLModel

from app.models.enums import Comment_status, Comment_target_type


class Comments(SQLModel, table=True):
    __tablename__ = "comments"
    __table_args__ = (
        CheckConstraint(
            "((target_type = 'anime' AND series_id IS NOT NULL AND episode_id IS NULL) "
            "OR (target_type = 'episode' AND episode_id IS NOT NULL AND series_id IS NULL))",
            name="ck_comments_target_type_matches_target",
        ),
        CheckConstraint(
            "((parent_comment_id IS NULL AND depth = 0) "
            "OR (parent_comment_id IS NOT NULL AND depth > 0 AND root_comment_id IS NOT NULL))",
            name="ck_comments_thread_shape",
        ),
        CheckConstraint("depth >= 0 AND depth <= 5", name="ck_comments_depth_limit"),
        Index("ix_comments_user_id", "user_id"),
        Index("ix_comments_series_id", "series_id"),
        Index("ix_comments_episode_id", "episode_id"),
        Index("ix_comments_parent_comment_id", "parent_comment_id"),
        Index("ix_comments_root_path", "root_comment_id", "path"),
        Index("ix_comments_status_created_at", "status", "created_at"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    target_type: Comment_target_type = Field(nullable=False)
    series_id: int | None = Field(default=None, foreign_key="anime_series.id")
    episode_id: int | None = Field(default=None, foreign_key="episodes.id")
    parent_comment_id: int | None = Field(default=None, foreign_key="comments.id")
    root_comment_id: int | None = Field(default=None, foreign_key="comments.id")
    depth: int = Field(default=0, nullable=False)
    path: str | None = Field(default=None, max_length=500)
    reply_to_user_id: int | None = Field(default=None, foreign_key="users.id")
    content: str = Field(nullable=False)
    status: Comment_status = Field(default=Comment_status.visible, nullable=False)
    is_deleted: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
    moderated_by: int | None = Field(default=None, foreign_key="users.id")
    moderated_at: datetime | None = None
