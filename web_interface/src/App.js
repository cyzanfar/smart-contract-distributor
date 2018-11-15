import React, { Component } from 'react';
import {Route, Switch, BrowserRouter} from 'react-router-dom';
import VestVault from "./components/VestVault";
import NotFound from "./components/NotFound";
import { Provider } from "react-redux";
import { createStore } from "redux";
import VestVaultApp from "./reducers";
import logo from './logo.svg';
import './App.css';

let store = createStore(VestVaultApp);

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <BrowserRouter>
        <Switch>
          <Route exact path="/" component={VestVault} />
          <Route component={NotFound} />
        </Switch>
        </BrowserRouter>
      </Provider>
    );
  }
}

export default App;
