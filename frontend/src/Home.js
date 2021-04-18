import React, {useEffect, useState} from 'react'
import {useHistory} from 'react-router-dom'

const Home = () => {
    const [product, setProduct] = useState({})

    const fetchData = async () => {
        const res = await fetch('/api/prod/')
        const data = await res.json()
        const prod = data[0]
        console.log(prod)
        setProduct(prod)

    }

    useEffect(() => {
        fetchData()
    }, [])

    const buyHandler = () => {
        history.push({
            pathname: '/product',
            state: {product}
        })
    }

    const history = useHistory()
    return (
        <div>
            <h1>List of Products</h1>
            <div>
                <h2>Name - {product.name}</h2>
                <h2>Price - {product.price}</h2>
                <h3>quantity - {product.quantity}</h3>
            <button onClick={buyHandler} >Buy This</button>
            </div>
        </div>
    )
}

export default Home
