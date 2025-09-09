import React from 'react'
import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <section>
      <h2>Welcome to Somoim</h2>
      <p>Find and create groups for your interests.</p>
      <Link to="/groups">Explore Groups</Link>
    </section>
  )
}
