# Screen Design Plan

## Overview
Somoim is a community platform for discovering and organizing interest-based groups and events.

### Core Flows
- **Authentication**: Users sign up or log in.
- **Group Discovery**: Browse groups, view details, and join.
- **Group Management**: Create new groups and manage membership.
- **Profile**: Users manage their profile and see their groups.
- **Group Interaction**: Members create events, RSVP, and post on the group board.

## Screen List
1. **Home** – Landing page with welcome text and quick access to groups.
2. **Group List** – Lists all groups with links to each group's detail page.
3. **Group Detail** – Shows group information, join button, events with RSVP, and board link.
4. **Group Board** – Free board for member posts.
5. **Create Post** – Form to add a new board post.
6. **Create Event** – Members schedule group events.
7. **Create Group** – Form to create a new group.
8. **Login** – Email/password login form.
9. **Sign Up** – Registration form for new users.
10. **Profile** – Displays user information and joined groups.
11. **404 Not Found** – Displayed when an unknown route is visited.

## Layout Sketches
### Home
```
+-------------------------------+
| Somoim                        |
+-------------------------------+
| Welcome text                  |
| [Explore Groups]              |
+-------------------------------+
| © 2024 Somoim                 |
+-------------------------------+
```

### Group List
```
Header/Nav
[Group links...]
```

### Group Detail
```
Header/Nav
Group title
Group description
[Join Group]
[Board]
Upcoming Events
- Event title – date [Going] [Not Going]
[Create Event]
```

### Group Board
```
Header/Nav
Board title
[Post list...]
[New Post]
```

### Create Post
```
Header/Nav
Form fields: title, content
[Post]
```

### Create Event
```
Header/Nav
Form fields: event title
[Save]
```

### Create Group
```
Header/Nav
Form fields: group name
[Create]
```

### Login
```
Header/Nav
Email
Password
[Login]
```

### Sign Up
```
Header/Nav
Email
Password
Confirm password
[Create Account]
```

### Profile
```
Header/Nav
User info
Membership list
```

## Navigation
- Global header with links: Home, Groups, Create Group, Profile, Login, Sign Up.
- Footer shows copyright notice.

## Notes
- Implementation uses placeholder data and minimal styling.
- Any group member can create events.
