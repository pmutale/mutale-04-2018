import React from 'react'
import ReactDOM from 'react-dom'
import "../../../scss/main";
import { hot } from 'react-hot-loader'
import Base from './components/base'
import ErrorBoundary from './components/error_boundary/error_boundary'


const renderApp = (ErrorBoundary) => {
  ReactDOM.render(
    <ErrorBoundary>
      <Base/>
    </ErrorBoundary>,
    document.getElementById('root'),
  )
};
hot(module)(renderApp(ErrorBoundary));