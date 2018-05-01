import React from 'react';
import ReactDOM from 'react-dom';
import '../../../scss/main';
import { AppContainer } from 'react-hot-loader';
import Base from './components/base';

const injectPoint = document.getElementById('root');

const renderApp = Component => {
  ReactDOM.render(
    <AppContainer>
      <Component
        current={injectPoint.getAttribute('data-pre-current')}
        language={injectPoint.getAttribute('data-language-page')}
      />
    </AppContainer>,
    injectPoint
  );
};

renderApp(Base);

if (module.hot) {
  module.hot.accept('./components/base', () => {
    renderApp(Base);
    renderApp(require('./components/base'));
  });
}
// hot(module)(renderApp(ErrorBoundary));