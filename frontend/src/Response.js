import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router'

const Response = () => {
    const [txnResponse, setTransactionRespone] = useState({})
    const { txnid } = useParams()
    
    const fetchTransactionDetail = async () => {
        const res = await fetch(`/api/response/${txnid}/`)
        const txnDetails = await res.json()
        setTransactionRespone(txnDetails)
    }

    useEffect(() => {
        fetchTransactionDetail()
        console.log(txnResponse)
    }, [])

    return (
        <div>
            <h1>Payment { txnResponse.status }</h1>
            <h2>Transaction ID : { txnResponse.txnid }</h2>
        </div>
    )
}

export default Response
