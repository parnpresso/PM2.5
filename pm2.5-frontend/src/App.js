import React, { Component } from 'react';
import Card from './components/Card';
import './App.css';

class App extends Component {
	state = {
		'city': 'Bangkok',
		'pm_value': 112,
		'pm_level': 6,
		'timestamp': 'timestamp',
	}

	render() {
		return (
			<div className="App">
				<Card city={this.state.city} 
				timestamp={this.state.timestamp} pm_value={this.state.pm_value} 
				pm_level={this.state.pm_level} />
			</div>
		);
	}
}

export default App;
