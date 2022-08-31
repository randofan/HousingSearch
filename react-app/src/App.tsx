import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import Search from './components/Search';
import './styles/App.css';
import MapManager from './components/MapManager';
import ResultPane from './components/ResultPane';

function App() {
  return (
    <div className="App">
        <Search></Search>
        <ResultPane></ResultPane>
        <MapManager />
    </div>
  );
}

export default App;
