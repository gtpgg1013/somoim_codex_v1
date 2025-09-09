import React from 'react'

export default function SignUp() {
  return (
    <section>
      <h2>Sign Up</h2>
      <form>
        <label>
          Email
          <input type="email" />
        </label>
        <label>
          Password
          <input type="password" />
        </label>
        <label>
          Confirm Password
          <input type="password" />
        </label>
        <button type="submit">Create Account</button>
      </form>
    </section>
  )
}
