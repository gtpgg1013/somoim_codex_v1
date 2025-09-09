import React from 'react'

export default function CreateGroup() {
  return (
    <section>
      <h2>Create Group</h2>
      <form>
        <label>
          Group Name
          <input type="text" placeholder="Enter group name" />
        </label>
        <button type="submit">Create</button>
      </form>
    </section>
  )
}
