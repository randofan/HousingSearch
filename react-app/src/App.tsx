import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import Search from './Search';
import './styles/App.css';
import MapManager from './MapManager';

function App() {
  return (
    <div className="App">
        <Search></Search>
        <MapManager></MapManager>
        {/* <li className="map-container">
          <ul></ul>
        </li> */}
    </div>
  );
}

export default App;
