import React, { useEffect, useState } from 'react'
import { useHistory } from 'react-router'

const Product = () => {

    useEffect(() => {
        generateHash()
    }, [])

    const history = useHistory()

    const [productDetails, setProductDetails] = useState({
        // txnid: "4TGnVaMrKb8Xnf",
        // key: "gtKFFx",
        // salt: "eCwWELxi",
        amount: "10.00",
        firstname: "first",
        email: "test@gmail.com",
        phone: "9876543210",
        productinfo: "Iphone",
        surl: "http://localhost:3000/api/response/",
        furl: "http://localhost:3000/api/response/"
    })

    const generateHash = async () => {
        const body = JSON.stringify(productDetails)
        const res = await fetch('api/payload/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Header": "*"
            },
            body
        })
        const data = await res.json()
        console.log(data)
        console.log(typeof body)
        history.push({
            pathname: '/checkout',
            state: {data}
        })
    }

    return (
        <div className='Product'>
            <h1>Product Details</h1>

            <button >Checkout</button>
        </div>
    )
}

export default Product
