import React, { useState } from "react";
import './styles/search.css';

export default function Search() {
    return (
        <div className="bar-container">
            <SearchBar></SearchBar>
            <FilterBar>
                <FilterBarItem title="Beds" options={["Studio", "1+ Beds", "2+ Beds", "3+ Beds", "4+ Beds"]}></FilterBarItem>
                <FilterBarItem title="Max Price" options={["Any", "$300", "$400", "$500", "$600", "$700", "$800"]}></FilterBarItem>
                <FilterBarItem title="Type" options={["Apartment", "Townhouse", "House"]}></FilterBarItem>
                <FilterBarItem title="More"></FilterBarItem>
            </FilterBar>
        </div>
    )
}

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

function FilterBarItem(props: any) {

    let options = [];
    options.push(<option hidden>{props.title}</option>);
    if (props.options != null) {
        for (let i = 0; i < props.options.length; i++) {
          options.push(<option>{props.options[i]}</option>);
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
