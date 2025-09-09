import React from 'react'
import { useParams } from 'react-router-dom'

export default function CreateEvent() {
  const { id } = useParams()
  return (
    <section>
      <h2>Create Event for Group {id}</h2>
      <form>
        <input placeholder="Event title" />
        <button type="submit">Save</button>
      </form>
    </section>
  )
}
