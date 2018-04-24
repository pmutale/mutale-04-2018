import React from 'react'
import ReactDOM from 'react-dom'
import "../../../scss/main";
import { hot } from 'react-hot-loader'
import Header from './components/header/header';


const renderApp = (Component) => {
    ReactDOM.render(
        <Component/>,
        document.getElementById('root'),
    )
};
hot(module)(renderApp(Header));