# Database Schema

This document outlines the core database tables used by the Somoim application.

## users
- `id` (PK)
- `email` (unique)
- `password_hash`
- `nickname`
- `created_at`
- `updated_at`

## groups
- `id` (PK)
- `name`
- `description`
- `owner_id` (FK -> users.id)
- `created_at`
- `updated_at`

## group_members
- `user_id` (FK -> users.id)
- `group_id` (FK -> groups.id)
- `role`
- `joined_at`
- Composite PK (`user_id`, `group_id`)

## posts
- `id` (PK)
- `group_id` (FK -> groups.id)
- `author_id` (FK -> users.id)
- `title`
- `content`
- `created_at`
- `updated_at`

## comments
- `id` (PK)
- `post_id` (FK -> posts.id)
- `author_id` (FK -> users.id)
- `content`
- `created_at`

## events
- `id` (PK)
- `group_id` (FK -> groups.id)
- `title`
- `description`
- `location`
- `start_time`
- `end_time`
- `created_at`

## event_participants
- `event_id` (FK -> events.id)
- `user_id` (FK -> users.id)
- `status`
- `joined_at`
- Composite PK (`event_id`, `user_id`)

## notifications
- `id` (PK)
- `user_id` (FK -> users.id)
- `type`
- `data` (JSON)
- `is_read`
- `created_at`
