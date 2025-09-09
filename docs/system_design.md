# System Design

This system uses a Python backend with SQLite for persistent storage.

## Architecture Overview

- **Client**: React single-page application served with Vite.
- **Reverse Proxy**: Nginx or a cloud load balancer routes requests to the API.
- **Application Layer**: FastAPI under Uvicorn workers organized into routers, services, and repositories.
- **Database**: SQLite for development; PostgreSQL or MySQL for production deployments.
- **Cache**: Redis for session storage, caching, and rate limiting.
- **Message Broker**: Celery workers backed by Redis or RabbitMQ handle background jobs such as email and push notifications.
- **Object Storage**: AWS S3 or similar service for user-uploaded images.
- **External Providers**: OAuth identity providers and email/SMS gateways.

### Request Flow
1. Client sends an HTTP request to the reverse proxy.
2. The proxy forwards the request to FastAPI, which validates input and routes to the appropriate handler.
3. Handlers interact with the database or cache; heavy tasks are enqueued to the message broker.
4. FastAPI returns a response while background workers process queued jobs and emit notifications.

## Database Schema

1. **users**
   - `id` (PK), `email`, `password_hash`, `nickname`, `created_at`, `updated_at`
   - Optional: `role` column or a separate `roles` table for permissions.

2. **groups (somoim)**
   - `id` (PK), `name`, `description`, `category`, `owner_id (FK → users.id)`, `created_at`, `updated_at`
   - Optional fields: group image, visibility (public/private), max members.

3. **group_members**
   - `user_id (FK → users.id)`, `group_id (FK → groups.id)`, `role` (owner/admin/member), `joined_at`
   - Composite PK: (`user_id`, `group_id`).

4. **posts**
   - `id` (PK), `group_id (FK → groups.id)`, `author_id (FK → users.id)`, `title`, `content`, `created_at`, `updated_at`

5. **comments**
   - `id` (PK), `post_id (FK → posts.id)`, `author_id (FK → users.id)`, `content`, `created_at`

6. **events**
   - `id` (PK), `group_id (FK → groups.id)`, `title`, `description`, `location`, `start_time`, `end_time`, `created_at`

7. **event_participants**
   - `event_id (FK → events.id)`, `user_id (FK → users.id)`, `status` (going/interested), `joined_at`
   - Composite PK: (`event_id`, `user_id`).

8. **notifications**
   - `id` (PK), `user_id (FK → users.id)`, `type`, `data` (JSON), `is_read`, `created_at`

## Backend Features

1. **Authentication & User Management**
   - Sign up, login, password reset.
   - JWT token issuance and refresh.
   - Profile update and deletion.

2. **Group Management**
   - Create, update, delete groups (owner only).
   - List and search groups with category filters.
   - Invite, join, leave groups; manage member roles.

3. **Posts & Comments**
   - CRUD for posts and comments within groups.
   - Optional image uploads to external storage.
   - Reporting mechanism for inappropriate content.

4. **Events**
   - Create, update, delete group events.
   - Join or cancel participation.
   - Calendar view API for schedules.

5. **Notifications**
   - Triggered by invitations, comments, event participation, etc.
   - Support for web/mobile push notifications.
   - Track read/unread status.

6. **Asynchronous Processing**
   - Background workers handle email delivery, push notifications, and other time-consuming tasks.
   - Scheduled jobs clean up stale data and rebuild recommendation indexes.

7. **Search & Recommendations**
   - Search groups, posts, users (consider search engine integration).
   - Recommend groups based on interests.

8. **Admin Tools**
   - User/group statistics, handling reports.
   - View logs, enforce bans or removals.

## Technology Stack

- **Backend**: Python (FastAPI).
- **Database**: SQLite (optional Redis for caching).
- **ORM**: SQLAlchemy.
- **API Style**: RESTful (GraphQL optional).
- **CI/CD**: GitHub Actions or GitLab CI for automated tests and deployment.
- **Deployment**: Docker containers on Kubernetes or AWS ECS/Fargate.

## Non-Functional Requirements

- Security: SSL/TLS, input validation, CSRF/XSS protection, rate limiting, and role-based access control.
- Scalability: Modular services with horizontal scaling and a message queue for intensive workloads.
- Performance: Caching frequently used queries, pagination, and minimizing N+1 database calls.
- Reliability: Regular backups and health checks with automatic restarts.
- Logging/Monitoring: Centralized logs (ELK), metrics (Prometheus + Grafana), and distributed tracing.
- Testing: Unit/integration tests, contract tests for external services, API documentation via Swagger/OpenAPI.
- Maintainability: Clear module boundaries and adherence to coding standards.

## Future Enhancements

- Real-time group chat using WebSockets.
- Event reminders via calendar integrations and push notifications.
- Geo-based group discovery and location-aware recommendations.
