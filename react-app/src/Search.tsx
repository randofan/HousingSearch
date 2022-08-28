import React, { useState } from "react";
import './styles/search.css';

export default function Search() {
    return (
        <div className="bar-container">
            <SearchBar></SearchBar>
            <FilterBar>
                <FilterBarItem name="Beds">
                    <Dropdown>
                        <DropdownSection type="radio" name="radios" items={["Studio", "1 bed", "2 beds", "3 beds"]}>
                        </DropdownSection>
                    </Dropdown>
                </FilterBarItem>
                <FilterBarItem name="Max Price">
                    <Dropdown>
                        <DropdownSection type="number">
                        </DropdownSection>
                    </Dropdown>
                </FilterBarItem>
                <FilterBarItem name="Type">
                    <Dropdown></Dropdown>
                </FilterBarItem>
                <FilterBarItem name="More">
                    <Dropdown>
                        <DropdownSection type="checkbox" title="Bathrooms" items={["1+ baths", "2+ baths", "3+ baths"]}></DropdownSection>
                        <DropdownSection type="checkbox" title="Pet Policy" items={["Dogs", "Cats", "No Pets"]}></DropdownSection>
                        <hr></hr>
                        <DropdownSection type="checkbox" title="Other" items={["Laundry in unit", "Parking"]}></DropdownSection>
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
    return (
        <div className="dropdown">
            {props.children}
        </div>
    )
}

function DropdownSection(props: any) {
    let arr: string[] = props.items;
    let items = [];
    if (props.type === "checkbox" || props.type === "radio") {
        for (let i = 0; i < arr.length; i++) {
            items.push(<label className="item-label"><input type={props.type} name={props.name}></input>{arr[i]}</label>);
        }
    }
    return (
        <div className="dropdown-section">
            <h3>{props.title}</h3>
            {items}
        </div>
    )
}