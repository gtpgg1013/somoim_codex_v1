import React from 'react'
import { useParams } from 'react-router-dom'

export default function CreatePost() {
  const { id } = useParams()
  return (
    <section>
      <h2>New Post for Group {id}</h2>
      <form>
        <label>
          Title
          <input type="text" />
        </label>
        <label>
          Content
          <textarea />
        </label>
        <button type="submit">Post</button>
      </form>
    </section>
  )
}
