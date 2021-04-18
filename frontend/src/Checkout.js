import React from 'react'
import { useLocation } from 'react-router'

const Checkout = () => {

    const location = useLocation()
    const {data, hash} = location.state.data
    console.log(location.state.data)

    return (
        <div>
            <form action='https://test.payu.in/_payment' method='POST'>
                <input type='hidden' name='key' value={data.key} />
                <input type='hidden' name='txnid' value={data.txnid} />
                <input type='hidden' name='amount' value={data.amount} />
                <input type='hidden' name='firstname' value={data.firstname} />
                <input type='hidden' name='email' value={data.email} />
                <input type='hidden' name='phone' value={data.phone} />
                <input type='hidden' name='productinfo' value={data.productinfo} />
                <input type='hidden' name='surl' value={data.surl} />
                <input type='hidden' name='furl' value={data.furl} />
                <input type='hidden' name='hash' value={hash} />
                <button style={{marginTop: '20px'}} type='submit'>Pay using PayuMoney</button>
            </form>
        </div>
    )
}

export default Checkout
