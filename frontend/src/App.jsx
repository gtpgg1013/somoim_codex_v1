import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import Groups from './pages/Groups'
import GroupDetail from './pages/GroupDetail'
import GroupBoard from './pages/GroupBoard'
import CreatePost from './pages/CreatePost'
import CreateEvent from './pages/CreateEvent'
import CreateGroup from './pages/CreateGroup'
import Profile from './pages/Profile'
import Login from './pages/Login'
import SignUp from './pages/SignUp'
import NotFound from './pages/NotFound'

export default function App() {
  return (
    <BrowserRouter>
      <header>
        <h1>Somoim</h1>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/groups">Groups</Link>
          <Link to="/create-group">Create Group</Link>
          <Link to="/profile">Profile</Link>
          <Link to="/login">Login</Link>
          <Link to="/signup">Sign Up</Link>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/groups" element={<Groups />} />
          <Route path="/groups/:id" element={<GroupDetail />} />
          <Route path="/groups/:id/board" element={<GroupBoard />} />
          <Route path="/groups/:id/board/new" element={<CreatePost />} />
          <Route path="/groups/:id/events/new" element={<CreateEvent />} />
          <Route path="/create-group" element={<CreateGroup />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <footer>© 2024 Somoim</footer>
    </BrowserRouter>
  )
}
