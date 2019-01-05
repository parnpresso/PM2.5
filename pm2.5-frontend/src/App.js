import React, { Component } from 'react';
import Card from './components/Card';
import './App.css';

const APIurl = 'http://0f54a4ea.ngrok.io/cities';

fetch(APIurl)
	.then((response) => response.json())
	.then(function(data) {
		console.log(data);
		// this.setState({
		// 	'city': data.city,
		// 	'pm_value': data.pm_value,
		// 	'pm_level': data.pm_level,
		// 	'timestamp': data.timestamp,	
		// });
	})
	.catch((error) => console.log(error));
		  
class App extends Component {
	state = {
		'city': 'Bangkok',
		'pm_value': 0,
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
