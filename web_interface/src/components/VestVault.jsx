import React, { Component } from 'react';
import {Link} from 'react-router-dom';


export default class VestVault extends Component {
  render() {
  return (
    <div>
    <h2>VestVault - Your trusted Smart Contract</h2>
    <p>
      <Link to="/contact">Click Here</Link> to contact us!
    </p>
    </div>
  )
  }
}
