import React from 'react'
import {useHistory} from 'react-router-dom'

const Home = () => {

    const history = useHistory()
    return (
        <div>
            <h1>List of Products</h1>
            <div onClick={() => history.push('/product')}>
                <h2>Product - 1</h2>
                <h2>Product - 2</h2>
            </div>
        </div>
    )
}

export default Home
