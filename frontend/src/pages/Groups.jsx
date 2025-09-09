import React from 'react'
import { Link } from 'react-router-dom'

const groups = [
  { id: 1, name: 'Reading Club' },
  { id: 2, name: 'Hiking Crew' },
]

export default function Groups() {
  return (
    <section>
      <h2>Groups</h2>
      <ul>
        {groups.map((g) => (
          <li key={g.id}>
            <Link to={`/groups/${g.id}`}>{g.name}</Link>
          </li>
        ))}
      </ul>
    </section>
  )
}
