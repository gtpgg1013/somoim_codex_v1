import React from 'react'
import { useParams, Link } from 'react-router-dom'

export default function GroupBoard() {
  const { id } = useParams()
  return (
    <section>
      <h2>Group {id} Board</h2>
      <p>Members can share posts here.</p>
      <Link to={`/groups/${id}/board/new`}>
        <button>New Post</button>
      </Link>
    </section>
  )
}
