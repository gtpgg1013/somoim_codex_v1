# Somoim App

Initial setup for a small group (somoim) application.

## Backend

- [FastAPI](https://fastapi.tiangolo.com/)
- SQLite via SQLAlchemy

### Run

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend

- [React](https://react.dev/) with [Vite](https://vitejs.dev/)
- Placeholder screens for group lists, details, board posts, events, and sign-up.

### Run

```bash
cd frontend
npm install
npm run dev
```

## Docs

- [Screen design](docs/SCREEN_DESIGN.md)
