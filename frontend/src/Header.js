import React from 'react'
import { useHistory } from 'react-router'

const Header = () => {
    const history = useHistory()
    return (
        <div className='Header'>
            <h1 onClick={() => history.push('/')} >Home</h1>
        </div>
    )
}

export default Header
