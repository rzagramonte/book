import { Link } from 'react-router-dom'

interface NavProps {
  isLoggedIn: boolean
}

const Nav = ({ isLoggedIn }: NavProps) => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        {isLoggedIn ? (
          <>
            <li><Link to="/dashboard">Dashboard</Link></li>
            <li><Link to="/profile">Profile</Link></li>
            <li><Link to="/logout">Logout</Link></li>
          </>
        ) : (
          <>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/learn">Learn</Link></li>
            <li><Link to="/safety">Safety</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/signup">Sign Up</Link></li>
          </>
        )}
      </ul>
    </nav>
  )
}

export default Nav
