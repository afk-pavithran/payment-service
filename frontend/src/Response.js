import React from 'react'
import { useParams } from 'react-router'

const Response = () => {
    const {txnid} = useParams()
    return (
        <div>
            <h1>Payment Success or Failure</h1>
            <h2>Transaction ID : { txnid }</h2>
        </div>
    )
}

export default Response
