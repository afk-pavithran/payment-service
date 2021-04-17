import React from 'react'
import { useLocation } from 'react-router'

const Checkout = () => {

    const location = useLocation()
    const {data, hash} = location.state.data
    console.log(location.state.data)

    return (
        <div>
            <form action='https://test.payu.in/_payment' method='POST'>
                <input name='key' value={data.key} />
                <input name='txnid' value={data.txnid} />
                <input name='amount' value={data.amount} />
                <input name='firstname' value={data.firstname} />
                <input name='email' value={data.email} />
                <input name='phone' value={data.phone} />
                <input name='productinfo' value={data.productinfo} />
                <input name='surl' value={data.surl} />
                <input name='furl' value={data.furl} />
                <input name='hash' value={hash} />
                <input type='submit' value='submit' />
            </form>
        </div>
    )
}

export default Checkout
