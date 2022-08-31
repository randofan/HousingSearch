import React, { useState } from "react";
import '../styles/search.css';

export default function Search() {
    return (
        <div className="bar-container">
            <SearchBar></SearchBar>
            <FilterBar>
                <FilterBarSelect title="Beds" options={["Studio", "1+ Beds", "2+ Beds", "3+ Beds", "4+ Beds"]}></FilterBarSelect>
                <FilterBarSelect title="Max Price" options={["Any", "$300", "$400", "$500", "$600", "$700", "$800"]}></FilterBarSelect>
                <FilterBarSelect title="Type" options={["Apartment", "Townhouse", "House"]}></FilterBarSelect>
                <FilterBarSelect title="More"></FilterBarSelect>
                <button className="clear-button">Clear</button>
            </FilterBar>
        </div>
    )
}
// TODO: figure out "more" format........
// a clear filter button
// how to send info from here...
// create result window --- how will i access state from input form......
// how to connect backend..?
// how to get map to respond ....... and show markers....coordinates from address
// navbar i guess -- idk if we need more than one page

function SearchBar() {
    return (
        <div className="searchbar">
            <input type="text" className="search" placeholder="Enter a city, state, or zip code."></input>
            <button className="button">Search</button>
        </div>
    )
}

function FilterBar(props: any) {
    return (
        <nav className="filterbar">
            <ul className="filterbar-list">
                <form id="filter-form">
                    {props.children}
                </form>
            </ul>
        </nav>
    )
}

function FilterBarSelect(props: any) {
    let options = [];
    options.push(<option hidden>{props.title}</option>);
    if (props.options != null) {
        for (let i = 0; i < props.options.length; i++) {
            options.push(<option key={i}>{props.options[i]}</option>);
        }
    }
    return (
        <li className="filterbar-item">
            <select className="filter-select">
                {options}
            </select>
        </li>
    )
}
