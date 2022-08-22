import React from "react";
import './styles/home.css';

export default function Home() {
    return (
        <div className="search-bar">
            <input type="text" className="search" placeholder="Enter a city, state, or zip code."></input>
            <button className="button">Search</button>
        </div>
    )
}