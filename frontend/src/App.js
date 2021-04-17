import logo from './logo.svg';
import './App.css';
import Header from './Header';
import { Route, Switch } from 'react-router';
import Home from './Home';
import Product from './Product';
import Checkout from './Checkout';
import Response from './Response';

function App() {
  return (
    <div className="App">
      <Header />
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/product' component={Product} />
        <Route path='/checkout' component={Checkout} />
        <Route path='/payment-status' component={Response} />
      </Switch>
    </div>
  );
}

export default App;
