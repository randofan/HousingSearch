import React, { useState } from "react";
import './styles/search.css';

export default function Search() {
    return (
        <div className="bar-container">
            <SearchBar></SearchBar>
            <FilterBar>
                <FilterBarItem name="Beds">
                    <Dropdown>
                        <DropdownSection type="checkbox" items={["hey", "dies", "bruh"]}>
                        </DropdownSection>
                    </Dropdown>
                </FilterBarItem>
                <FilterBarItem name="Price">
                    <Dropdown></Dropdown>
                </FilterBarItem>
                <FilterBarItem name="Type">
                    <Dropdown></Dropdown>
                </FilterBarItem>
                <FilterBarItem name="More">
                    <Dropdown>
                        <DropdownSection type="checkbox" name="Bathrooms" items={["1+ baths", "2+ baths", "3+ baths"]}></DropdownSection>
                        <DropdownSection type="checkbox" name="Pet Policy" items={["Dogs", "Cats", "No Pets"]}></DropdownSection>
                        <hr></hr>
                        <DropdownSection type="checkbox" name="Pet Policy" items={["Dogs", "Cats", "No Pets"]}></DropdownSection>
                    </Dropdown>
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

function Dropdown(props: any) {
    // should pass in array of what you want??? ie. checkbox, etc.
    // loop to render it all?
    return (
        <div className="dropdown">
            {props.children}
        </div>
    )
}



function DropdownSection(props: any) {
    let arr: string[] = props.items;
    let items = [];
    for (let i = 0; i < arr.length; i++) {
        items.push(<label className="item-label"><input type={props.type}></input>{arr[i]}</label>);
    }
    return (
        <div className="dropdown-section">
            <h3>{props.name}</h3>
            {items}
        </div>
    )
}