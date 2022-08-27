import React, {useState} from "react";
import './styles/home.css';

export default function Home() {
    return (
        <div className="bar-container">
            <SearchBar></SearchBar>
            <FilterBar>
                <FilterBarItem name="Beds">
                    <Dropdown><p>hi</p></Dropdown>
                </FilterBarItem>
                <FilterBarItem name="Price">
                    <Dropdown></Dropdown>
                </FilterBarItem>
                <FilterBarItem name="Type">
                    <Dropdown></Dropdown>
                </FilterBarItem>
                <FilterBarItem name="More">
                    <Dropdown></Dropdown>
                </FilterBarItem>
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
            <ul className="filterbar-list">{props.children}</ul>
        </nav>
    )
}

function FilterBarItem(props: any) {
    const [open, setOpen] = useState(false);

    return (
        <li className="filterbar-item">
            <button onClick={() => setOpen(!open)}>{props.name}</button>
            {open && props.children}
        </li>
    )
}

function Dropdown(props:any) {
    // should pass in array of what you want??? ie. checkbox, etc.
    // loop to render it all?
    return (
        <div className="dropdown">
            {props.children}
        </div>
    )
}