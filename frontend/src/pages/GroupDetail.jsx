import React from 'react'
import { useParams, Link } from 'react-router-dom'

const groups = [
  { id: 1, name: 'Reading Club', description: 'Discuss books monthly.' },
  { id: 2, name: 'Hiking Crew', description: 'Weekend hikes in the mountains.' },
]

const events = [
  { id: 1, title: 'Kick-off Meeting', date: '2024-07-01' },
  { id: 2, title: 'Monthly Hike', date: '2024-07-15' },
]

export default function GroupDetail() {
  const { id } = useParams()
  const group = groups.find((g) => g.id === Number(id))

  if (!group) {
    return <p>Group not found.</p>
  }

  return (
    <section>
      <h2>{group.name}</h2>
      <p>{group.description}</p>
      <button>Join Group</button>
      <nav>
        <Link to={`/groups/${id}/board`}>Board</Link>
      </nav>
      <h3>Upcoming Events</h3>
      <ul>
        {events.map((e) => (
          <li key={e.id}>
            {e.title} - {e.date}
            <button>Going</button>
            <button>Not Going</button>
          </li>
        ))}
      </ul>
      <Link to={`/groups/${id}/events/new`}>
        <button>Create Event</button>
      </Link>
    </section>
  )
}
