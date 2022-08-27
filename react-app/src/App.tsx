import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import Home from './Home';
import './styles/App.css';
import MapManager from './MapManager';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Home></Home>
        <MapManager></MapManager>
      </header>
    </div>
  );
}

export default App;
