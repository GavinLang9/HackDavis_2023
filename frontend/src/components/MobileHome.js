import React from "react";
import { useState, useEffect } from "react";
import ListItem from "./ListItem";
import '../css/mobileHome.css'
import { Link } from 'react-router-dom'

const MobileHomePage = () => {
    const [locationText, setLocationText] = useState('')
    const [date, setDate] = useState()
    const [searchText, setSearchText] = useState('')
    const [recents, setRecents] = useState([])

    const handleSearchChange = (e) => {
        setSearchText(e.target.value)
        
        console.log(e)
    }

    const handleDateChange = (e) => {
        setDate(e.target.value)
        console.log(e)
    }

    useEffect(
        ()=> {
            fetch('/event/getRecents', {
                method: 'GET',
                
            })
            .then(response=>response.json())
            .then(data=> {
                let list = [data[0],data[1],data[2],data[3],data[4]]
                setRecents(list)
                console.log(recents)
            })
        }, []
    )

    return ( 
        <div className="home">
            <div className="nav">
                {/* Logo */}
                <h1 className="title">Yolo County Food Resources</h1>
            </div>
            <form>
            <div className="textInput">
                <input type="search" id="location" name="location" onChange={handleSearchChange} value={locationText} placeholder="Enter Location"/>
                <input type="datetime-local" id="date" name="date" onChange={handleDateChange} value={date}/>
            </div>
            <div className="row">
            <select name="tags" id="tags">
                <option value="student">Student</option>
                <option value="income">Income</option>
            </select>
            <input className="submit" type="submit" value="Search" />
            </div>
            </form>
            <div className="recurringorsingular">
                <input className="recurring" type="button" value="Recurring" />
                <input className="singular" type="button" value="Singular"  />
            </div>
            <div className="event-container">
            {recents.map((eve) => {
                console.log(eve.id)
                return (
                <ListItem props={eve} key={eve.id}/>
                )
            })}
            </div>
            <button>
            <Link className="linkToCreateEvent" to="/CreateEvent">Create Event</Link>
            </button>
            
            
            
        </div>
    )
}

export default MobileHomePage