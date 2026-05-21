from enum import Enum


class User_Role(str, Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"


class User_status(str, Enum):
    active = "active"
    email_unverified = "email_unverified"
    suspended = "suspended"
    banned = "banned"
    deleted = "deleted"


class User_gender(str, Enum):
    male = "male"
    female = "female"


class Season_name(str, Enum):
    Spring = "Spring"
    Summer = "Summer"
    Fall = "Fall"
    Winter = "Winter"


class Anime_status(str, Enum):
    ongoing = "ongoing"
    completed = "completed"
    upcoming = "upcoming"


class Content_access_type(str, Enum):
    free = "free"
    premium = "premium"


class Episode_access_type(str, Enum):
    inherit = "inherit"
    free = "free"
    premium = "premium"


class Episode_status(str, Enum):
    processing = "processing"
    ready = "ready"
    error = "error"


class Category_type(str, Enum):
    genre = "genre"
    tag = "tag"


class Media_purpose(str, Enum):
    avatar = "avatar"
    cover = "cover"
    banner = "banner"
    thumbnail = "thumbnail"
    episode_thumbnail = "episode_thumbnail"


class Media_status(str, Enum):
    active = "active"
    archived = "archived"
    deleted = "deleted"


class Notification_type(str, Enum):
    new_episode = "new_episode"
    reply_comment = "reply_comment"
    membership = "membership"
    moderation = "moderation"
    system = "system"


class Notification_ref_type(str, Enum):
    anime = "anime"
    episode = "episode"
    comment = "comment"
    membership = "membership"
    payment = "payment"
    report = "report"


class weekday(str, Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"


class ReportStatus(str, Enum):
    pending = "pending"
    reviewing = "reviewing"
    resolved = "resolved"
    rejected = "rejected"


class UserReportReason(str, Enum):
    spam = "spam"
    toxic = "toxic"
    harassment = "harassment"
    advertising = "advertising"
    other = "other"


class EpisodeReportReason(str, Enum):
    broken_video = "broken_video"
    missing_subtitle = "missing_subtitle"
    wrong_subtitle = "wrong_subtitle"
    wrong_content = "wrong_content"
    dead_link = "dead_link"
    policy_violation = "policy_violation"
    other = "other"


class Plan_status(str, Enum):
    active = "active"
    inactive = "inactive"
    archived = "archived"


class Membership_status(str, Enum):
    pending = "pending"
    scheduled = "scheduled"
    active = "active"
    grace_period = "grace_period"
    expired = "expired"
    cancelled = "cancelled"
    refunded = "refunded"


class Payment_method(str, Enum):
    momo = "momo"
    vnpay = "vnpay"
    stripe = "stripe"
    paypal = "paypal"
    bank_transfer = "bank_transfer"


class Payment_status(str, Enum):
    pending = "pending"
    success = "success"
    failed = "failed"
    refunded = "refunded"


class Review_status(str, Enum):
    visible = "visible"
    hidden = "hidden"
    pending = "pending"
    deleted = "deleted"


class Comment_status(str, Enum):
    visible = "visible"
    hidden = "hidden"
    pending = "pending"
    deleted = "deleted"


class Comment_target_type(str, Enum):
    anime = "anime"
    episode = "episode"


class Moderation_action_type(str, Enum):
    hide_comment = "hide_comment"
    restore_comment = "restore_comment"
    hide_review = "hide_review"
    restore_review = "restore_review"
    ban_user = "ban_user"
    unban_user = "unban_user"
    resolve_report = "resolve_report"
    reject_report = "reject_report"


class Audit_action(str, Enum):
    user_login = "user_login"
    payment_webhook = "payment_webhook"
    membership_activated = "membership_activated"
    moderation_action = "moderation_action"
    admin_update = "admin_update"
